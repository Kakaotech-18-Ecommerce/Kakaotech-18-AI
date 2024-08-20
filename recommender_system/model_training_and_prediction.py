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
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(),
        "Lasso Regression": Lasso(),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
        "XGBoost": XGBRegressor(random_state=42),
        "LightGBM": LGBMRegressor(
            random_state=42,
            min_gain_to_split=0.001,
            min_data_in_leaf=1,
            max_depth=3,
            force_col_wise=True
        ),
        "SVM": SVR(),
        "KNN": KNeighborsRegressor(),
    }

    # 각 모델을 평가하고 예측값을 저장하기 위한 리스트 초기화
    predictions = []

    # 모델 평가 및 예측
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        predictions.append(y_pred)

        mse, mae, rmse, r2, mape = evaluate_model(model, X_train, X_test, y_train, y_test)
        print(f'{name} - MSE: {mse}, MAE: {mae}, RMSE: {rmse}, R-squared: {r2}, MAPE: {mape}')

    # 앙상블(평균 앙상블) 예측
    ensemble_prediction = np.mean(predictions, axis=0)

    # 최종 앙상블 모델의 성능 평가
    ensemble_mse = mean_squared_error(y_test, ensemble_prediction)
    ensemble_mae = mean_absolute_error(y_test, ensemble_prediction)
    ensemble_rmse = np.sqrt(ensemble_mse)
    ensemble_r2 = r2_score(y_test, ensemble_prediction)
    ensemble_mape = mean_absolute_percentage_error(y_test, ensemble_prediction)

    print(f'Ensemble - MSE: {ensemble_mse}, MAE: {ensemble_mae}, RMSE: {ensemble_rmse}, R-squared: {ensemble_r2}, MAPE: {ensemble_mape}')

    # 최종 예측을 위해 전체 데이터에 대해 앙상블 모델 적용
    all_predictions = []
    for model in models.values():
        all_predictions.append(model.predict(X_scaled))  # 가중치가 적용된 데이터 사용
    final_ensemble_prediction = np.mean(all_predictions, axis=0)

    filtered_data['predicted_review_star'] = final_ensemble_prediction

    return filtered_data, ensemble_mse  # 앙상블 모델의 MSE를 반환
