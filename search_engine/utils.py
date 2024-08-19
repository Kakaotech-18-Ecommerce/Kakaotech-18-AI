# utils.py 파일은 프로젝트에서 공통적으로 사용할 유틸리티 함수들을 정의

import logging
from config import LOG_FILE

def setup_logging():
    """로그 설정 함수."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    logger = logging.getLogger()
    return logger

def validate_query(query_str):
    """검색어가 유효한지 확인하는 함수."""
    if not query_str.strip():
        raise ValueError("검색어가 비어있습니다.")
    return query_str.strip()

def format_results(results):
    """검색 결과를 포맷팅하여 출력하는 함수."""
    formatted_results = []
    for result in results:
        formatted_results.append({
            "Product ID": result.get("product_id"),
            "Product Name": result.get("product_name"),
            "Explanation": result.get("product_explanation"),
            "Category": result.get("category"),
            "Predicted Review Star": result.get("predicted_review_star", 'N/A')
        })
    return formatted_results

def print_results(results):
    """포맷된 검색 결과를 출력하는 함수."""
    for result in results:
        print(f"Product ID: {result['Product ID']}")
        print(f"Product Name: {result['Product Name']}")
        print(f"Explanation: {result['Explanation']}")
        print(f"Category: {result['Category']}")
        print(f"Predicted Review Star: {result['Predicted Review Star']}")
        print("-" * 20)
