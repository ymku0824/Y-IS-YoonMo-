from sqlalchemy.exc import SQLAlchemyError
from models import db, Video

def save_metadata(video_id, metadata):
    """PostgreSQL에 메타데이터 저장"""
    try:
        video = Video(
            video_id=video_id,
            user_id=metadata['user_id'],
            category=metadata['category'],
            status=metadata['status'],
            file_url=metadata['file_url'],
            transcription=metadata['transcription'],
            summary=metadata['summary']
        )
        db.session.add(video)
        db.session.commit()
        print(f"[INFO] 비디오 메타데이터 저장 완료: {video_id}")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"[ERROR] 메타데이터 저장 실패: {e}")

def get_metadata(video_id):
    """PostgreSQL에서 메타데이터 가져오기"""
    try:
        video = Video.query.filter_by(video_id=video_id).first()
        if video:
            return {
                "video_id": video.video_id,
                "user_id": video.user_id,
                "category": video.category,
                "status": video.status,
                "file_url": video.file_url,
                "transcription": video.transcription,
                "summary": video.summary
            }
        return None
    except SQLAlchemyError as e:
        print(f"[ERROR] 메타데이터 가져오기 실패: {e}")
        return None