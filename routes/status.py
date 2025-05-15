# routes/status.py
from flask import Blueprint, jsonify
from models.video import Video

status_bp = Blueprint('status', __name__)

@status_bp.route('/status/<video_id>', methods=['GET'])
def get_video_status(video_id):
    try:
        video = Video.query.get(video_id)
        if not video:
            return jsonify({'error': 'Video not found'}), 404
        return jsonify({'video_id': video.video_id, 'status': video.status, 'metadata': {
            'user_id': video.user_id,
            'category': video.category,
            'summary': video.summary,
            'file_url': video.file_url
        }}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
