# edit.py - Allows editing of chapter titles and metadata
from flask import Blueprint, request, jsonify
from services.db_service import save_metadata, get_metadata

edit_bp = Blueprint('edit', __name__)

@edit_bp.route('/edit/<video_id>', methods=['PATCH'])
def edit_video(video_id):
    try:
        data = request.get_json()
        new_metadata = data.get('metadata', {})

        # Retrieve existing metadata
        metadata = get_metadata(video_id)
        if not metadata:
            return jsonify({'error': 'Video metadata not found'}), 404

        # Update metadata with new data
        metadata.update(new_metadata)

        # Save updated metadata
        save_metadata(video_id, metadata)
        return jsonify({'message': 'Metadata updated successfully', 'video_id': video_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
