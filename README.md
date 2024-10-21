![Golla Golla](https://github.com/user-attachments/assets/99136f2e-f17e-435c-ae1f-96d15b46937e)
# 골라골라 RecSys & Search Engine API

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 목적](#프로젝트-목적)
3. [주요 기능](#주요-기능)
4. [사용된 기술 및 라이브러리](#사용된-기술-및-라이브러리)
5. [설치 방법](#설치-방법)
6. [실행 방법](#실행-방법)
7. [API 사용법](#API-사용법)
8. [개발 과정](#개발-과정)
9. [파일 구조](#파일-구조)

## 프로젝트 개요
이 프로젝트는 간식/과자 등의 제품에 대해 머신러닝 모델을 사용하여 사용자 리뷰 점수를 예측하는 추천 시스템과, 제품 이름이나 설명을 기반으로 관련 제품을 검색할 수 있는 검색 엔진을 포함합니다. Flask 프레임워크를 사용하여 API 형태로 배포되며, 클라이언트는 이 API를 통해 제품 데이터를 업로드하고 예측된 리뷰 점수를 받아보거나 관련 제품을 검색할 수 있습니다.

## 프로젝트 목적
- 머신러닝을 사용하여 제품 리뷰 점수를 예측하고, 이를 기반으로 사용자에게 추천할 수 있는 시스템을 개발합니다.
- Flask를 사용하여 API 형태로 배포함으로써 클라이언트가 쉽게 데이터를 업로드하고 결과를 받을 수 있도록 합니다.
- 제품 이름이나 설명을 기반으로 관련된 제품을 검색할 수 있는 검색 엔진을 제공합니다.

## 주요 기능
- **데이터 업로드**: 제품 데이터를 업로드하여 추천 시스템에 학습시킵니다.
- **리뷰 점수 예측**: 업로드된 데이터를 바탕으로 각 제품의 리뷰 점수를 예측합니다.
- **예측 결과 반환**: 예측된 리뷰 점수와 제품 ID를 반환합니다.
- **예측 결과 파일 제공**: 예측 결과를 파일로 제공하는 API를 통해 클라이언트가 결과를 다운로드할 수 있습니다.
- **검색 엔진**: 제품의 이름이나 설명을 기반으로 관련된 제품을 검색합니다.
- **정렬 기능**: 검색 결과는 `predicted_review_star`를 기준으로 내림차순 정렬됩니다.

## 사용된 기술 및 라이브러리
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- XGBoost
- LightGBM
- Whoosh (검색 엔진용)

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
pip install -r requirements.txt
```

## 실행 방법

### 1. 인덱스 생성 (검색 엔진용)
```bash
python search_engine/index.py
```

### 2. 서버 실행
```bash
python app.py
```

서버는 기본적으로 `http://127.0.0.1:5001`에서 실행됩니다.

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

### 4. 제품 검색 (검색 엔진)
- **엔드포인트**: `/search`
- **HTTP 메소드**: `POST`
- **설명**: 제품의 이름이나 설명을 기반으로 관련된 제품을 검색합니다.
- **예시**:
```bash
curl -X POST http://127.0.0.1:5001/search \
-H "Content-Type: application/json" \
-d '{"query": "초콜릿"}'
```

### 5. GET 방식으로 제품 검색
- **엔드포인트**: `/search`
- **HTTP 메소드**: `GET`
- **설명**: 제품의 이름이나 설명을 기반으로 관련된 제품을 검색합니다.
- **예시**:
```bash
curl "http://127.0.0.1:5001/search?query=초콜릿"
```

## 개발 과정

### 1. 데이터 로드 및 전처리
- 추천 시스템의 데이터를 JSON 파일로부터 로드하여 Pandas DataFrame으로 변환합니다.
- 필요한 특성들에 가중치를 적용하고, 모델 학습을 위해 데이터를 스케일링합니다.

### 2. 모델 학습 및 예측
- 다양한 머신러닝 모델을 사용하여 제품 리뷰 점수를 예측합니다.
  - 선형 회귀, Ridge, Lasso, Random Forest, Gradient Boosting, XGBoost, LightGBM 등.
- 예측된 결과를 바탕으로 앙상블 모델을 통해 최종 점수를 예측합니다.

### 3. 검색 엔진 구현
- Whoosh 라이브러리를 사용하여 제품 이름 및 설명에 대한 인덱스를 생성합니다.
- 사용자가 입력한 쿼리를 기반으로 관련 제품을 검색하고 `predicted_review_star` 기준으로 결과를 정렬합니다.

### 4. 결과 저장 및 반환
- 예측된 리뷰 점수를 JSON 및 CSV 파일로 저장합니다.
- 클라이언트의 요청에 따라 예측 결과를 반환하거나 검색 결과를 제공합니다.

## 파일 구조
```bash

/project-root
├── Research (EDA & Test_Model)          # 모델 테스트와 탐색적 데이터 분석(EDA) 노트북 디렉토리
│   ├── Kakao_RecSys_Test_Model.ipynb    # 추천 시스템 모델 테스트 노트북
│   ├── Output_Data                      # 모델 테스트 결과 데이터를 저장하는 디렉토리
│   │   ├── Kakao_Recsys_Output.csv      # 모델 출력 CSV 파일
│   │   ├── product_predictions.json     # 예측된 제품 리뷰 점수를 저장한 JSON 파일
│   │   └── product_predictions_only_score.json  # 리뷰 점수만 저장된 JSON 파일
├── app.py                               # Flask 애플리케이션 메인 파일, 검색 엔진 및 추천 시스템 블루프린트 등록
├── dummy_data                           # 테스트 및 샘플 데이터 저장 디렉토리
│   ├── products.json                    # 테스트용 제품 데이터 JSON 파일
├── recommender_system                   # 추천 시스템 관련 코드 및 데이터 디렉토리
│   ├── Output_Data                      # 추천 시스템의 예측 결과 저장 디렉토리
│   │   ├── Kakao_Recsys_Output.csv      # 예측 결과 CSV 파일
│   │   ├── model_training_results.csv   # 모델 학습 결과 CSV 파일
│   │   ├── product_id_with_predictions.json  # 예측된 리뷰 점수와 제품 ID를 포함한 JSON 파일
│   │   └── product_predictions.json     # 최종 예측 결과 JSON 파일
│   ├── category_based_recommendation.py # 카테고리 기반 추천 시스템 모듈
│   ├── data_loading_and_preprocessing.py  # 데이터 로드 및 전처리 모듈
│   ├── main.py                          # 추천 시스템 실행 파일
│   ├── model_training_and_prediction.py # 모델 학습 및 예측 모듈
│   ├── routes.py                        # 추천 시스템 관련 Flask 라우트 정의
│   ├── save_results.py                  # 예측 결과를 파일로 저장하는 모듈
│   ├── similarity_and_recommendation.py # 유사도 계산 및 추천 모듈
├── requirements.txt                     # 프로젝트 의존성 패키지 목록
├── search_engine                        # 검색 엔진 관련 코드 디렉토리
│   ├── config.py                        # 검색 엔진 설정 파일
│   ├── index.py                         # 검색 인덱스를 생성하는 스크립트
│   ├── routes.py                        # 검색 엔진 관련 Flask 라우트 정의
│   ├── search_engine.py                 # 검색 엔진 메인 모듈
│   ├── utils.py                         # 검색 엔진 유틸리티 함수 모음
└── tests                                # 테스트 코드 디렉토리
    ├── conftest.py                      # 테스트 설정 파일
    └── test_search_engine.py            # 검색 엔진 관련 테스트 코드
```
---
