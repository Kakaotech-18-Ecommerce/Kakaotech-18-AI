from flask import Blueprint, request, jsonify, Response
import json
from search_engine.search_engine import search

# 블루프린트 생성
search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/search', methods=['POST', 'GET'])
def search_api():
    if request.method == 'POST':
        data = request.get_json()
        query = data.get('query', '')
    elif request.method == 'GET':
        query = request.args.get('query', '')

    # 검색 엔진 호출, 카테고리 필터는 사용하지 않음
    results = search(query)

    response_data = {
        'query': query,
        'results': results
    }
    response_json = json.dumps(response_data, ensure_ascii=False)
    return Response(response_json, content_type='application/json; charset=utf-8')
