from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 서버 설정
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv("MAX_CONTENT_LENGTH"))

# DB 설정
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB 초기화
from models.db import db
db.init_app(app)

# 블루프린트 등록
from routes.upload import upload_bp
from routes.summarize import summarize_bp
from routes.edit import edit_bp
from routes.status import status_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(upload_bp)
app.register_blueprint(summarize_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(status_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def index():
    return "PostgreSQL 연동 테스트 페이지"

if __name__ == "__main__":
    app.run(debug=True)