import pandas as pd

def get_category_recommendations(filtered_data, label_encoder):
    category_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    recommendations = {}

    for category, code in category_mapping.items():
        category_data = filtered_data[filtered_data['category_encoded'] == code].copy()
        if not category_data.empty:
            category_data['predicted_review_star'] = category_data['predicted_review_star'].round(2)
            recommendations[category] = category_data[['product_id', 'predicted_review_star']].sort_values(by='predicted_review_star', ascending=False)
        else:
            recommendations[category] = pd.DataFrame()  # No data found for this category
    
    return recommendations
