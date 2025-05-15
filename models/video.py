from models.db import db

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    file_url = db.Column(db.String(255), nullable=False)
    transcription = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Video {self.video_id}>"