from data_loading_and_preprocessing import load_and_preprocess_data
from model_training_and_prediction import train_and_predict
from similarity_and_recommendation import calculate_similarity_and_recommend
from category_based_recommendation import print_category_recommendations
from save_results import save_to_csv, save_to_json

def main():
    # 데이터 로드 및 전처리
    products_df, label_encoder = load_and_preprocess_data('/path/to/products.json')
    
    # 모델 학습 및 예측
    filtered_data, mse = train_and_predict(products_df)
    print(f'Mean Squared Error: {mse}')
    
    # 카테고리별 추천
    print_category_recommendations(filtered_data, label_encoder)

    # 결과 저장
    save_to_csv(filtered_data, 'Kakao_Recsys_Output.csv')
    save_to_json(products_df, filtered_data, 'product_predictions.json')

if __name__ == "__main__":
    main()
