from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import pickle
from database import Database

# Load hybrid model
with open('models/hybrid_recommender.pkl', 'rb') as f:
    hybrid_model = pickle.load(f)

cf_model = hybrid_model['cf_model']
cosine_sim = hybrid_model['content_sim']
tfidf = hybrid_model['tfidf']
product_indices = hybrid_model['product_indices']
products_df = hybrid_model['products_df']

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize the database
db = Database(users_file="users.csv", products_file="products.csv")


# Hybrid recommendations function
def hybrid_recommendations(user_id, top_n=5, weight_cf=0.7, weight_cb=0.3):
    # Collaborative filtering predictions
    product_ids = products_df['product_id'].unique()
    cf_scores = []
    for product_id in product_ids:
        pred = cf_model.predict(user_id, product_id)
        cf_scores.append((product_id, pred.est))
    cf_scores = sorted(cf_scores, key=lambda x: x[1], reverse=True)[:top_n]

    # Content-based recommendations
    user_history = db.get_user_history(user_id)['product_id'].tolist()
    cb_scores = []
    for product_id in user_history:
        if product_id in product_indices:
            idx = product_indices[product_id]
            similarity_scores = list(enumerate(cosine_sim[idx]))
            similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
            top_indices = [i[0] for i in similarity_scores[1:top_n + 1]]
            cb_scores.extend(products_df.iloc[top_indices]['product_id'].tolist())

    # Combine scores
    hybrid_scores = {}
    for product_id, score in cf_scores:
        hybrid_scores[product_id] = hybrid_scores.get(product_id, 0) + score * weight_cf
    for product_id in cb_scores:
        hybrid_scores[product_id] = hybrid_scores.get(product_id, 0) + weight_cb

    # Sort by hybrid score and return top N
    hybrid_scores = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)
    recommended_product_ids = [product_id for product_id, _ in hybrid_scores[:top_n]]
    return products_df[products_df['product_id'].isin(recommended_product_ids)]


# Route to get recommendations
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))

    # If the user doesn't exist, return top products
    user_history = db.get_user_history(user_id)
    if user_history.empty:
        top_products = db.get_top_products(n=5).to_dict(orient='records')
        return jsonify({"status": "success", "recommendations": top_products})

    # Generate hybrid recommendations
    recommendations = hybrid_recommendations(user_id, top_n=5)
    return jsonify({"status": "success", "recommendations": recommendations.to_dict(orient='records')})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
