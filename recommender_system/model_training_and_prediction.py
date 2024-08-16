from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

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

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # 전체 데이터에 대한 추천 점수 계산
    X_all_weighted = X * weights  # 전체 데이터에 가중치 적용
    X_all_scaled = scaler.transform(X_all_weighted)  # 스케일링 적용
    filtered_data['predicted_review_star'] = model.predict(X_all_scaled)

    return filtered_data, mse
