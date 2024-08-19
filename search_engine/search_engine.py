from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from whoosh.query import Term

# 검색 기능 구현
def search(query_str, category_filter=None):
    # 인덱스 열기
    index = open_dir("search_engine/data/index")
    
    # 여러 필드를 동시에 검색할 수 있도록 MultiFieldParser 설정
    parser = MultifieldParser(["product_name", "product_explanation", "category"], index.schema)

    with index.searcher() as searcher:
        query = parser.parse(query_str)

        # 카테고리 필터링 기능 추가
        if category_filter:
            category_query = Term("category", category_filter)
            query = query & category_query

        results = searcher.search(query)
        
        # 검색 결과를 출력
        for result in results:
            print(f"Product ID: {result['product_id']}")
            print(f"Product Name: {result['product_name']}")
            print(f"Explanation: {result['product_explanation']}")
            print(f"Category: {result['category']}")
            print("-" * 20)

# 예시 검색
if __name__ == "__main__":
    query = input("Enter your search query: ")
    category = input("Enter category to filter (or press Enter to skip): ")
    search(query, category_filter=category if category else None)