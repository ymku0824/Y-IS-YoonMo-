# dashboard.py - Displays the list of processed videos and their status
from flask import Blueprint, jsonify
from models.video import Video
from app import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    try:
        videos = []
        # Query all video metadata from PostgreSQL
        video_records = Video.query.all()
        for video in video_records:
            videos.append({
                'video_id': video.video_id,
                'user_id': video.user_id,
                'category': video.category,
                'status': video.status,
                'file_url': video.file_url
            })
        return jsonify({'videos': videos}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500