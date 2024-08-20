from flask import Blueprint, request, jsonify, Response
import json
from search_engine.search_engine import search

# 블루프린트 생성
search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/search', methods=['POST'])
def search_api():
    data = request.get_json()
    query = data.get('query', '')
    category_filter = data.get('category_filter', None)

    results = search(query, category_filter)

    response_data = {
        'query': query,
        'category_filter': category_filter,
        'results': results
    }
    response_json = json.dumps(response_data, ensure_ascii=False)
    return Response(response_json, content_type='application/json; charset=utf-8')
