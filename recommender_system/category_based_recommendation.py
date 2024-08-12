def print_category_recommendations(filtered_data, label_encoder):
    category_mapping = dict(zip(label_encoder.classes_, range(len(label_encoder.classes_))))
    
    for category, code in category_mapping.items():
        category_data = filtered_data[filtered_data['category_encoded'] == code].copy()
        if not category_data.empty:
            category_data['predicted_review_star'] = category_data['predicted_review_star'].round(2)
            print(f"Category: {category}")
            print(category_data[['product_id', 'predicted_review_star']].sort_values(by='predicted_review_star', ascending=False))
            print("\n")
        else:
            print(f"No data found for category: {category}")
