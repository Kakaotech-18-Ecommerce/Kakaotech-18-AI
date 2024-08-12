import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)
    
    # 전처리 단계
    label_encoder = LabelEncoder()
    df['category'] = label_encoder.fit_transform(df['category'])
    df = df.dropna(subset=['review_star'])

    return df, label_encoder