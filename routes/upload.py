# routes/upload.py
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import uuid

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_video():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        category = request.form.get('category', 'default')
        user_id = request.form.get('user_id', 'anonymous')

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, str(uuid.uuid4()), filename)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)

        return jsonify({'message': '비디오 업로드 성공', 'file_path': file_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
