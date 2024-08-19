import sys
import os

# 현재 파일의 디렉토리 위치를 기준으로 상위 디렉토리 (프로젝트 루트) 경로를 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
