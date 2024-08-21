# 골라골라 추천 시스템 (Recommender System)

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 목적](#프로젝트-목적)
3. [주요 기능](#주요-기능)
4. [사용된 기술 및 라이브러리](#사용된-기술-및-라이브러리)
5. [설치 방법](#설치-방법)
6. [실행 방법](#실행-방법)
7. [추천 시스템 방식 & Architecture](#추천-시스템-방식--Architecture)
8. [API 사용법](#API-사용법)
9. [개발 과정](#개발-과정)
10. [파일 구조](#파일-구조)

## 프로젝트 개요
이 프로젝트는 제품 데이터에 대해 머신러닝 모델을 사용하여 사용자 리뷰 점수를 예측하는 추천 시스템입니다. Flask 프레임워크를 사용하여 API 형태로 배포되며, 클라이언트는 이 API를 통해 제품 데이터를 업로드하고 예측된 리뷰 점수를 받아볼 수 있습니다.

## 프로젝트 목적
- 머신러닝을 사용하여 제품 리뷰 점수를 예측하고, 이를 기반으로 사용자에게 추천할 수 있는 시스템을 개발합니다.
- Flask를 사용하여 API 형태로 배포함으로써 클라이언트가 쉽게 데이터를 업로드하고 결과를 받을 수 있도록 합니다.

## 주요 기능
- **데이터 업로드**: 제품 데이터를 업로드하여 추천 시스템에 학습시킵니다.
- **리뷰 점수 예측**: 업로드된 데이터를 바탕으로 각 제품의 리뷰 점수를 예측합니다.
- **예측 결과 반환**: 예측된 리뷰 점수와 제품 ID를 반환합니다.
- **예측 결과 파일 제공**: 예측 결과를 파일로 제공하는 API를 통해 클라이언트가 결과를 다운로드할 수 있습니다.

## 사용된 기술 및 라이브러리
- **Python 3.x**
- **Flask**
- **Pandas**
- **Numpy**
- **Scikit-learn**
- **XGBoost**
- **LightGBM**

## 설치 방법

### 1. 클론 레포지토리
```bash
git clone https://github.com/your-repository.git
cd your-repository

### 2. 가상 환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. 필요한 패키지 설치
```bash
pip install -r recommender_system/requirements.txt
```

## 서버 실행
```bash
python app.py
```

서버가 실행되면 `http://127.0.0.1:5001`에서 API를 사용할 수 있습니다.

## 추천시스템 & Architecture

###  회귀 기반 추천 시스템
이 프로젝트는 **회귀 기반 추천 시스템**을 사용하여 제품의 리뷰 점수를 예측하고, 이를 기반으로 제품을 추천합니다. 이 접근법은 특정 사용자나 제품의 특성을 바탕으로 연속적인 예측 값을 생성하는 모델을 사용하여 추천을 제공합니다.

### 사용한 모델과 이유

#### 1. Linear Regression (선형 회귀 모델)
- **사용 이유**:
  - **단순성과 해석 가능성**: 선형 회귀 모델은 입력 변수와 출력 변수 간의 관계를 선형 함수로 표현하며, 이로 인해 모델이 직관적이고 해석하기 쉽습니다.
  - **회귀 기반 접근**: 제품의 특성(`product_price`, `product_inventory`, `discount`, `product_quanity`)을 입력으로 받아 `review_star`(사용자 리뷰 점수)라는 연속적인 값을 예측하는 데 적합합니다..
  - **실제 적용 사례**: 선형 회귀는 예측이 필요한 다양한 도메인에서 널리 사용되며, 특히 연속적인 타겟 값을 예측하는 데 유리합니다..

#### 2. 다른 모델 사용 가능성
- **다양한 모델의 사용 가능성**: 프로젝트에서는 Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost, LightGBM 등의 다양한 회귀 모델을 실험했습니다.
- **평가 지표의 중요성**: 다양한 평가 지표(MSE, MAE, RMSE, R²)를 사용해 모델의 성능을 평가하며, 비즈니스 목표에 가장 잘 맞는 지표를 최종 선택했습ㄴ디ㅏ..

### Hybrid Approach (혼합 접근법)의 가능성
- **확장 가능성**: 현재 시스템은 회귀 기반이지만, 협업 필터링과 같은 다른 추천 시스템 기법을 혼합하여 하이브리드 접근법으로 확장할 가능성도 열어두었습니다 (추후 확장 대비).
- **예시**: 협업 필터링 기법을 결합하거나, 콘텐츠 기반 필터링에 추가적인 사용자 데이터를 통합하는 방식으로 시스템의 정확성과 개인화를 향상시킬 수 있습니다..

### 평가 지표

- **MSE와 RMSE**: 평균 제곱 오차와 루트 평균 제곱 오차는 예측 값과 실제 값 간의 차이를 측정하는 데 사용되며, 큰 오차에 대해 더 큰 패널티를 부여합니다.
- **MAE**: 평균 절대 오차는 각 예측 오차의 절대값을 평균내어 계산하여, 이상치에 덜 민감하며 직관적인 오차 해석을 제공합니다.
- **R² 및 Adjusted R²**: 모델이 타겟 변수의 변동성을 얼마나 설명하는지를 나타내며, 특히 Adjusted R²는 과적합 방지에 유리합니다.

### Research 필요성
- 다양한 모델과 평가 지표를 실험하여, 최종적으로 어떤 지표와 모델이 비즈니스 목표에 가장 적합한지를 결정하는 연구가 필요합니다.

## API 사용법

### 1. 데이터 업로드 (추천 시스템)
- **엔드포인트**: `/recommend/upload-data`
- **HTTP 메소드**: `POST`
- **설명**: 클라이언트가 제품 데이터를 JSON 형태로 업로드합니다.
- **예시**:
```bash
curl -X POST http://127.0.0.1:5001/recommend/upload-data \
-H "Content-Type: application/json" \
-d "@/Users/your_username/path_to_your_json_file/products.json"
```

### 2. 예측 요청 (추천 시스템)
- **엔드포인트**: `/recommend/predict`
- **HTTP 메소드**: `POST`
- **설명**: 서버에 업로드된 데이터를 바탕으로 제품 리뷰 점수를 예측하고 결과를 반환합니다.
- **예시**:
```bash
curl -X POST http://127.0.0.1:5001/recommend/predict
```

### 3. 예측 결과 파일 가져오기 (추천 시스템)
- **엔드포인트**: `/recommend/send-predictions`
- **HTTP 메소드**: `GET`
- **설명**: 예측 결과 파일을 JSON 형식으로 반환합니다.
- **예시**:
```bash
curl -X GET http://127.0.0.1:5001/recommend/send-predictions
```

## 개발 과정

### 1. 데이터 로드 및 전처리
- data_loading_and_preprocessing.py에서 데이터를 로드하고, Pandas DataFrame으로 변환하여 필요한 전처리 작업을 수행합니다.
- 각 특성에 가중치를 부여하고, 모델 학습을 위해 데이터를 스케일링합니다.

### 2. 모델 학습 및 예측
- model_training_and_prediction.py에서 다양한 머신러닝 모델을 사용하여 제품 리뷰 점수를 예측합니다.
  - 선형 회귀, Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost, LightGBM 등을 포함합니다.
- 예측된 결과를 바탕으로 앙상블 모델을 통해 최종 점수를 예측합니다.

### 3. 결과 저장 및 반환
- save_results.py에서 예측된 리뷰 점수를 JSON 및 CSV 파일로 저장합니다.
- 클라이언트의 요청에 따라 routes.py에서 예측 결과를 반환합니다.

## 파일 구조
```bash
/recommender_system
├── Output_Data                      # 모델 결과 저장 디렉토리
│   ├── Kakao_Recsys_Output.csv      # 예측 결과 CSV 파일
│   ├── model_training_results.csv   # 모델 학습 결과 CSV 파일
│   ├── product_id_with_predictions.json  # 예측된 리뷰 점수와 제품 ID를 포함한 JSON 파일
│   └── product_predictions.json     # 최종 예측 결과 JSON 파일
├── __init__.py                      # 패키지 초기화 파일
├── category_based_recommendation.py # 카테고리 기반 추천 시스템 모듈
├── data_loading_and_preprocessing.py  # 데이터 로드 및 전처리 모듈
├── dummy_data                       # 테스트용 더미 데이터 디렉토리
│   └── products.json                # 더미 제품 데이터 JSON 파일
├── main.py                          # 추천 시스템 실행 파일
├── model_training_and_prediction.py # 모델 학습 및 예측 모듈
├── requirements.txt                 # 프로젝트 요구사항 파일
├── routes.py                        # Flask 블루프린트 정의      
├── save_results.py                  # 결과 저장 모듈
└── similarity_and_recommendation.py # 유사도 계산 및 추천 모듈
```
---
