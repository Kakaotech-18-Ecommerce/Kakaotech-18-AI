import json
import pandas as pd
from model_training_and_prediction import train_and_predict  # 모델 학습 및 예측 함수 임포트

def save_to_csv(filtered_data, output_filename):
    filtered_data.to_csv(output_filename, index=False)
    print(f"Data has been saved to {output_filename}")

def save_to_json(products, filtered_data, output_json_filename):
    if not isinstance(products, list):
        raise ValueError("Expected products to be a list of dictionaries")
    if not isinstance(filtered_data, pd.DataFrame):
        raise ValueError("Expected filtered_data to be a pandas DataFrame")
    
    for product in products:
        product_id = product['product_id']
        predicted_star = filtered_data.loc[filtered_data['product_id'] == product_id, 'predicted_review_star'].values
        if len(predicted_star) > 0:
            product['predicted_review_star'] = round(predicted_star[0], 2)  # 값을 반올림하여 추가

    with open(output_json_filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print(f"Updated JSON file has been saved to {output_json_filename}")

def save_filtered_json(filtered_data, output_json_filename):
    predicted_data = filtered_data[['product_id', 'predicted_review_star']].round(2)
    predicted_dict = predicted_data.to_dict(orient='records')
    with open(output_json_filename, 'w', encoding='utf-8') as f:
        json.dump(predicted_dict, f, ensure_ascii=False, indent=4)
    print(f"Filtered JSON file has been saved to {output_json_filename}")

def save_model_results_to_csv(results, output_filename):
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_filename, index=False)
    print(f"Model results have been saved to {output_filename}")
