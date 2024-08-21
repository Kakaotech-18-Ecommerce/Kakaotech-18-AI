# Kakaotech-18-AI Search Engine

이 프로젝트는 Kakaotech-18-AI의 검색 엔진을 구현한 것입니다. 사용자는 특정 제품의 이름이나 설명을 검색하여 관련된 제품을 찾을 수 있습니다.

## 주요 기능
- **검색 엔진**: 제품의 이름이나 설명을 기반으로 관련된 제품을 검색합니다.
- **정렬 기능**: 검색 결과는 `predicted_review_star`를 기준으로 내림차순 정렬됩니다.

## 프로젝트 구조

```plaintext
search_engine/
├── __init__.py
├── config.py                        # 설정 파일
├── data                             # 인덱스 및 로그 데이터
│   ├── index
│   │   ├── MAIN_WRITELOCK
│   │   ├── MAIN_gcvh748xna7xdg0t.seg
│   │   └── _MAIN_1.toc
│   ├── logs
│   │   └── search_engine.log        # 검색 엔진 로그 파일
├── index.py                         # 인덱싱 코드
├── routes.py                        # 검색 엔진 관련 API 라우트
├── search_engine.py                 # 검색 엔진 메인 파일
└── utils.py                         # 유틸리티 함수
```

### 구조 설명
- **`index.py`**: 검색 엔진에 필요한 인덱스를 생성하는 스크립트입니다.
- **`search_engine.py`**: 검색 기능을 구현한 메인 모듈입니다.
- **`routes.py`**: Flask를 통해 API로 검색 엔진을 사용할 수 있도록 라우트를 정의한 파일입니다.
- **`utils.py`**: 검색 엔진에서 사용하는 유틸리티 함수들이 정의된 파일입니다.

## 설치 및 실행 방법

### 1. 의존성 설치
프로젝트를 클론한 후, 필요한 패키지를 설치합니다.

```bash
git clone <repository-url>
cd Kakaotech-18-AI
pip install -r requirements.txt
```

### 2. 인덱스 생성
검색 엔진을 사용하기 전에 데이터를 인덱싱해야 합니다.

```bash
python search_engine/index.py
```

### 3. Flask 서버 실행
서버를 실행하여 API 엔드포인트를 활성화합니다.

```bash
python app.py
```

서버는 기본적으로 `http://127.0.0.1:5001`에서 실행됩니다.

## 사용법

### 1. 검색 엔진 사용
사용자는 `/search` 엔드포인트를 통해 제품을 검색할 수 있습니다.

**POST 요청 예시**:
```bash
curl -X POST http://127.0.0.1:5001/search \
-H "Content-Type: application/json" \
-d '{"query": "초콜릿"}'
```

**GET 요청 예시**:
```bash
curl "http://127.0.0.1:5001/search?query=초콜릿"
```

### 2. 검색 결과
검색 결과는 `predicted_review_star` 기준으로 내림차순 정렬되어 반환됩니다.

## 테스트

테스트를 실행하여 검색 엔진의 기능이 올바르게 작동하는지 확인할 수 있습니다.

```bash
PYTHONPATH=./ pytest tests/
```

이 명령어를 통해 모든 유닛 테스트가 실행됩니다.

## 기타

- **로깅**: 검색 엔진에서 발생하는 주요 이벤트는 `search_engine/data/logs/`에 기록됩니다.
- **데이터 파일**: 검색 인덱스는 `search_engine/data/index/`에 저장됩니다.

