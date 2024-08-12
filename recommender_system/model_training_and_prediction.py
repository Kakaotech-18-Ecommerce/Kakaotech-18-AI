from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_and_predict(filtered_data):
    features = ['product_price', 'product_inventory', 'discount', 'product_quanity']
    target = 'review_star'

    X = filtered_data[features]
    y = filtered_data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    filtered_data['predicted_review_star'] = model.predict(filtered_data[features])

    return filtered_data, mse
