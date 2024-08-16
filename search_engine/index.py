import json
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
import os

# 인덱스 스키마 정의 (필요한 필드만 포함)
schema = Schema(
    product_id=ID(stored=True, unique=True),  # product_id는 유일성이 필요하므로 포함
    product_name=TEXT(stored=True),  # 검색에 사용
    product_explanation=TEXT(stored=True),  # 검색에 사용
    category=TEXT(stored=True)  # 검색에 사용
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

# 인덱스에 데이터 추가
for product in products:
    writer.add_document(
        product_id=str(product["product_id"]),  # ID 필드는 문자열로 저장
        product_name=product["product_name"].strip().lower(),
        product_explanation=product["product_explanation"],
        category=product["category"]
    )

# 인덱스 커밋
writer.commit()

print("Indexing completed successfully.")
