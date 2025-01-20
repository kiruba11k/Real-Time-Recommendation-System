import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating synthetic data
fake = Faker()

# Constants
NUM_USERS = 1000  # Number of users
NUM_PRODUCTS = 500  # Number of products
NUM_RECORDS = 5000  # Number of user-product interactions

# Generate products.csv
def generate_products_csv():
    product_ids = range(1, NUM_PRODUCTS + 1)
    product_names = [f"Product {i}" for i in product_ids]
    categories = ["Electronics", "Clothing", "Home", "Books", "Toys", "Beauty"]
    prices = [round(random.uniform(10, 500), 2) for _ in product_ids]
    
    # Generate the same number of descriptions as products
    descriptions = [fake.text(max_nb_chars=50) for _ in product_ids]

    products_data = {
        "product_id": product_ids,
        "product_name": product_names,
        "description": descriptions,
        "category": [random.choice(categories) for _ in product_ids],
        "price": prices,
    }

    products_df = pd.DataFrame(products_data)
    products_df.to_csv("products.csv", index=False)
    print("Generated products.csv")

# Generate users.csv
def generate_users_csv():
    user_ids = range(1, NUM_USERS + 1)
    interactions = []

    for _ in range(NUM_RECORDS):
        user_id = random.choice(user_ids)
        product_id = random.randint(1, NUM_PRODUCTS)
        interaction = random.choice(["view", "add_to_cart", "purchase"])
        timestamp = fake.date_time_this_year()

        interactions.append({
            "user_id": user_id,
            "product_id": product_id,
            "interaction": interaction,  # Ensure correct column name here
            "timestamp": timestamp,
        })

    users_df = pd.DataFrame(interactions)
    users_df.to_csv("users.csv", index=False)
    print("Generated users.csv successfully")
# Generate both files
if __name__ == "__main__":
    generate_products_csv()
    generate_users_csv()
