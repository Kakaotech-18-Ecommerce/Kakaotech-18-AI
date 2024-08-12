import json
import pandas as pd

def save_to_csv(filtered_data, output_filename):
    filtered_data.to_csv(output_filename, index=False)
    print(f"Data has been saved to {output_filename}")

def save_to_json(products, filtered_data, output_json_filename):
    for product in products:
        product_id = product['product_id']
        predicted_star = filtered_data.loc[filtered_data['product_id'] == product_id, 'predicted_review_star'].values
        if len(predicted_star) > 0:
            product['predicted_review_star'] = predicted_star[0]

    with open(output_json_filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print(f"Updated JSON file has been saved to {output_json_filename}")
