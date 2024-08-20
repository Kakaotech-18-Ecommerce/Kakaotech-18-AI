from flask import Blueprint, request, jsonify
import os
import json
from .model_training_and_prediction import train_and_predict
from .data_loading_and_preprocessing import load_and_preprocess_data
from .save_results import save_to_json, save_model_results_to_csv

# 블루프린트 생성
recommend_bp = Blueprint('recommend', __name__)

# 데이터를 받아서 dummy_data에 저장하는 엔드포인트
@recommend_bp.route('/upload-data', methods=['POST'])
def upload_data():
    data = request.json
    file_path = 'recommender_system/dummy_data/products.json'
    
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 데이터를 파일에 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    return jsonify({"message": "Data has been successfully uploaded"}), 200

# 모델을 학습시키고 결과를 반환하는 엔드포인트
@recommend_bp.route('/predict', methods=['POST'])
def predict():
    file_path = 'recommender_system/dummy_data/products.json'
    
    # 데이터 로드 및 전처리
    products_df, label_encoder = load_and_preprocess_data(file_path)
    
    # 모델 학습 및 예측
    filtered_data, model_results_df = train_and_predict(products_df)

    # 결과 저장 경로 설정
    output_dir = 'recommender_system/Output_Data'
    os.makedirs(output_dir, exist_ok=True)

    # 결과 파일 경로 정의
    json_output_path = os.path.join(output_dir, 'product_predictions.json')
    results_csv_path = os.path.join(output_dir, 'model_training_results.csv')

    # 결과 저장
    products_list = products_df.to_dict(orient='records')
    save_to_json(products_list, filtered_data, json_output_path)
    save_model_results_to_csv(model_results_df, results_csv_path)

    # product_id와 predicted_review_star 값을 반환
    result = filtered_data[['product_id', 'predicted_review_star']].to_dict(orient='records')

    return jsonify({
        "predictions": result,
        "message": "Completion of model training results and recommendation scores"
    }), 200

# BE에 파일을 보내는 엔드포인트
@recommend_bp.route('/send-predictions', methods=['GET'])
def send_predictions():
    output_dir = 'recommender_system/Output_Data'
    product_predictions_path = os.path.join(output_dir, 'product_predictions.json')

    if os.path.exists(product_predictions_path):
        with open(product_predictions_path, 'r', encoding='utf-8') as f:
            product_predictions = json.load(f)
        
        return jsonify(product_predictions), 200
    else:
        return jsonify({"message": "Prediction file not found"}), 404
