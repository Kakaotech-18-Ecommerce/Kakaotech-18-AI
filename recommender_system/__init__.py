from flask import Flask
from .routes import recommender_bp

def create_app():
    app = Flask(__name__)
    
    # 블루프린트 등록
    app.register_blueprint(recommender_bp, url_prefix='/recommender')
    
    return app