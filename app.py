from flask import Flask
from search_engine.routes import search_bp

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(search_bp)

@app.route('/')
def home():
    return "Search Engine API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)