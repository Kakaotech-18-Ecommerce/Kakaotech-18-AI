import json
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
import os

# 인덱스 스키마 정의
schema = Schema(
    product_name=TEXT(stored=True),
    description=TEXT(stored=True),
    category=TEXT(stored=True),
    product_id=ID(stored=True, unique=True)
)

# 인덱스 디렉토리 설정
index_dir = "search_engine/data/index"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

# 인덱스 생성
index = create_in(index_dir, schema)
writer = index.writer()

# 데이터 로드 및 전처리
with open('dummy_data/products.json', 'r') as f:
    products = json.load(f)

# 데이터 전처리 (예: 텍스트 클리닝)
for product in products:
    product['product_name'] = product['product_name'].strip().lower()
    # 필요에 따라 추가적인 전처리 작업을 수행할 수 있습니다

# 인덱스에 데이터 추가
for product in products:
    writer.add_document(
        product_id=product["product_id"],
        product_name=product["product_name"],
        description=product["description"],
        category=product["category"]
    )

# 인덱스 커밋
writer.commit()

print("Indexing completed successfully.")
