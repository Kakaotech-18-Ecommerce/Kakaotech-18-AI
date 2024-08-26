from flask import Flask
from .routes import recommend_bp

def create_app():
    app = Flask(__name__)
    
    # 블루프린트 등록
    app.register_blueprint(recommend_bp, url_prefix='/recommender')
    
    return app