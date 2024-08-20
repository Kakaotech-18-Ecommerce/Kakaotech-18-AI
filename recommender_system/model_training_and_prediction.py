import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)

    return mse, mae, rmse, r2, mape

def train_and_predict(filtered_data):
    features = ['product_price', 'product_inventory', 'discount', 'product_quanity']
    target = 'review_star'

    X = filtered_data[features]
    y = filtered_data[target]

    # 특성에 가중치 적용
    weights = [8.0, 1.5, 1.5, 0.8]  # 각 특성에 적용할 가중치('product_price', 'product_inventory', 'discount', 'product_quanity')
    X_weighted = X * weights

    # 특성 스케일링
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_weighted)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 사용할 모델들 초기화
    models = {
        "Linear Regression": LinearRegression(), # 기본 선형 회귀 모델
        "Ridge Regression": Ridge(), # L2 정규화를 사용하는 선형 회귀
        "Lasso Regression": Lasso(), # L1 정규화를 사용하는 선형 회귀
        "Random Forest": RandomForestRegressor(random_state=42), # 여러 결정 트리의 앙상블을 사용하는 랜덤 포레스트
        "Gradient Boosting": GradientBoostingRegressor(random_state=42), # 약한 학습기를 순차적으로 학습시키는 그래디언트 부스팅
        "XGBoost": XGBRegressor(random_state=42), # 그래디언트 부스팅의 최적화된 구현
        "LightGBM": LGBMRegressor(), # 빠르고 효율적인 그래디언트 부스팅 구현
        "SVM": SVR(), # 서포트 벡터 머신을 이용한 회귀
        "KNN": KNeighborsRegressor(), # K-최근접 이웃 알고리즘을 이용한 회귀
    }

     # 각 모델의 결과 저장을 위한 딕셔너리 초기화
    results = {
        "Model": [],
        "MSE": [],
        "MAE": [],
        "RMSE": [],
        "R-squared": [],
        "MAPE": []
    }

    # 모델 평가 및 예측
    predictions = []
    for name, model in models.items():
        mse, mae, rmse, r2, mape = evaluate_model(model, X_train, X_test, y_train, y_test)
        results["Model"].append(name)
        results["MSE"].append(mse)
        results["MAE"].append(mae)
        results["RMSE"].append(rmse)
        results["R-squared"].append(r2)
        results["MAPE"].append(mape)
        predictions.append(model.predict(X_test))

        print(f'{name} - MSE: {mse}, MAE: {mae}, RMSE: {rmse}, R-squared: {r2}, MAPE: {mape}')


    # 앙상블(평균 앙상블) 예측
    ensemble_prediction = np.mean(predictions, axis=0)

    # 최종 앙상블 모델의 성능 평가
    ensemble_mse = mean_squared_error(y_test, ensemble_prediction)
    ensemble_mae = mean_absolute_error(y_test, ensemble_prediction)
    ensemble_rmse = np.sqrt(ensemble_mse)
    ensemble_r2 = r2_score(y_test, ensemble_prediction)
    ensemble_mape = mean_absolute_percentage_error(y_test, ensemble_prediction)

    # 앙상블 결과 추가
    results["Model"].append("Ensemble")
    results["MSE"].append(ensemble_mse)
    results["MAE"].append(ensemble_mae)
    results["RMSE"].append(ensemble_rmse)
    results["R-squared"].append(ensemble_r2)
    results["MAPE"].append(ensemble_mape)

    print(f'Ensemble - MSE: {ensemble_mse}, MAE: {ensemble_mae}, RMSE: {ensemble_rmse}, R-squared: {ensemble_r2}, MAPE: {ensemble_mape}')

    # 최종 예측을 위해 전체 데이터에 대해 앙상블 모델 적용
    all_predictions = []
    for model in models.values():
        all_predictions.append(model.predict(X_scaled))  
    final_ensemble_prediction = np.mean(all_predictions, axis=0)

    filtered_data['predicted_review_star'] = final_ensemble_prediction

    # 모델 평가 및 예측 결과를 DataFrame으로 변환
    results_df = pd.DataFrame(results)
    
    return filtered_data, results_df  # 모델 결과 DataFrame을 반환
