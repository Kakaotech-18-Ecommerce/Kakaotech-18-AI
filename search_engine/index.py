import json
from whoosh.fields import Schema, TEXT, ID, NUMERIC
from whoosh.index import create_in
import os
from config import INDEX_DIR, DATA_DIR  # 설정값 가져오기

# 인덱스 스키마 정의 (필요한 필드만 포함)
schema = Schema(
    product_id=ID(stored=True, unique=True),
    product_name=TEXT(stored=True),
    product_explanation=TEXT(stored=True),
    category=TEXT(stored=True),
    predicted_review_star=NUMERIC(stored=True, decimal_places=1)
)

# 인덱스 디렉토리 설정
if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)

# 인덱스 생성
index = create_in(INDEX_DIR, schema)
writer = index.writer()

# 데이터 로드 및 전처리
with open(DATA_DIR, 'r') as f:
    products = json.load(f)

# 인덱스에 데이터 추가
for product in products:
    writer.add_document(
        product_id=str(product["product_id"]),
        product_name=product["product_name"].strip().lower(),
        product_explanation=product["product_explanation"],
        category=product["category"],
        predicted_review_star=float(product["predicted_review_star"])
    )

# 인덱스 커밋
writer.commit()

print("Indexing completed successfully.")
