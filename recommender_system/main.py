from data_loading_and_preprocessing import load_and_preprocess_data
from model_training_and_prediction import train_and_predict
from similarity_and_recommendation import calculate_similarity_and_recommend, get_similar_items
from category_based_recommendation import print_category_recommendations
from save_results import save_to_csv, save_to_json, save_filtered_json
import os

def main():
    # 데이터 로드 및 전처리
    products_df, label_encoder = load_and_preprocess_data('/Users/daehyunkim_kakao/Desktop/Kakao Business (Project)/Kakaotech-18-AI/dummy_data/products.json')
    
    # 모델 학습 및 예측
    filtered_data, mse = train_and_predict(products_df)
    print(f'Mean Squared Error: {mse}')
    
    # 카테고리별 추천
    print_category_recommendations(filtered_data, label_encoder)

    # 결과 저장 경로 설정
    output_dir = '/Users/daehyunkim_kakao/Desktop/Kakao Business (Project)/Kakaotech-18-AI/recommender_system/Output_Data'
    os.makedirs(output_dir, exist_ok=True)  # 디렉토리가 없으면 생성

    # 결과 파일 경로 정의
    csv_output_path = os.path.join(output_dir, 'Kakao_Recsys_Output.csv')
    json_output_path = os.path.join(output_dir, 'product_predictions.json')
    filtered_json_output_path = os.path.join(output_dir, 'product_id_with_predictions.json')

    # 결과 저장
    products_list = products_df.to_dict(orient='records')
    save_to_csv(filtered_data, csv_output_path)
    save_to_json(products_list, filtered_data, json_output_path)
    save_filtered_json(filtered_data, filtered_json_output_path)

if __name__ == "__main__":
    main()
