# config.py는 프로젝트의 다양한 경로와 설정을 관리
import os

# 프로젝트 루트 디렉토리 경로
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 인덱스 디렉토리 경로
INDEX_DIR = os.path.join(BASE_DIR, 'search_engine', 'data', 'index')

# 데이터 파일 경로
DATA_DIR = os.path.join(BASE_DIR, 'Research (EDA & Test_Model)', 'Output_Data', 'product_predictions.json')

# 로그 파일 경로
LOG_FILE = os.path.join(BASE_DIR, 'search_engine', 'data', 'logs', 'search_engine.log')

# 기타 설정값
DEFAULT_SEARCH_FIELDS = ["product_name", "product_explanation", "category"]