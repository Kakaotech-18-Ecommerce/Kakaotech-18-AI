from flask import Flask
from search_engine.routes import search_bp
from recommender_system.routes import recommend_bp

app = Flask(__name__)

# 검색 엔진 블루프린트 등록
app.register_blueprint(search_bp)

# 추천 시스템 블루프린트 등록
app.register_blueprint(recommend_bp, url_prefix='/recommend')

@app.route('/')
def home():
    return "Search Engine & RecSys System API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
