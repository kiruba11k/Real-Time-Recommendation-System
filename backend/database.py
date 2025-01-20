import pandas as pd

class Database:
    def __init__(self, users_file, products_file):
        self.users_df = pd.read_csv(users_file)
        self.products_df = pd.read_csv(products_file)

    def get_user_history(self, user_id):
        return self.users_df[self.users_df['user_id'] == user_id]

    def get_top_products(self, n=5):
        # Example: Return products with the highest interaction count
        top_products = (
            self.users_df.groupby('product_id')
            .size()
            .sort_values(ascending=False)
            .head(n)
            .index
        )
        return self.products_df[self.products_df['product_id'].isin(top_products)]
