from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def calculate_similarity_and_recommend(products_df):
    user_item_matrix = products_df.pivot(index='member_id', columns='product_id', values='review_star').fillna(0)
    item_similarity = cosine_similarity(user_item_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

    return item_similarity_df

def get_similar_items(item_similarity_df, product_id, num_items=5):
    if product_id in item_similarity_df.index:
        similar_items = item_similarity_df[product_id].sort_values(ascending=False).head(num_items)
        return similar_items
    else:
        return f"Product ID {product_id} not found in the dataset"
