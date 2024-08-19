# Engine Test Module

import pytest
from search_engine.search_engine import search
from search_engine.config import INDEX_DIR
from whoosh.index import open_dir

@pytest.fixture
def setup_index():
    """인덱스를 미리 설정하는 pytest fixture."""
    index = open_dir(INDEX_DIR)
    return index

def test_search_functionality(setup_index):
    """기본 검색 기능을 테스트합니다."""
    results = search("초콜릿", category_filter=None)
    assert len(results) > 0, "검색 결과가 없습니다."

def test_category_filtering(setup_index):
    """카테고리 필터링 기능을 테스트합니다."""
    results = search("초콜릿", category_filter="간식/과자")
    assert all(result['category'] == "간식/과자" for result in results), "카테고리 필터링이 제대로 동작하지 않습니다."

def test_predicted_review_star_sorting(setup_index):
    """predicted_review_star로 정렬하는 기능을 테스트합니다."""
    results = search("초콜릿", category_filter=None)
    predicted_stars = [result['predicted_review_star'] for result in results]  # 일관된 변수명 사용
    assert predicted_stars == sorted(predicted_stars, reverse=True), "predicted_review_star 정렬이 제대로 동작하지 않습니다."


