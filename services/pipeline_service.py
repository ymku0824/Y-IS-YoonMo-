# pipeline_service.py - Integrates Whisper and GPT services into a single pipeline
import os
from services.whisper_service import transcribe_audio
from services.db_service import save_metadata
from services.gemini_service import generate_chapter_titles

def process_video(video_path, video_id, user_id, category):
    try:
        # Step 1: Define file path and upload folder
        upload_folder = f"static/uploads/{video_id}"
        os.makedirs(upload_folder, exist_ok=True)

        # Save the uploaded video to the local file system
        file_name = f"{video_id}.mp4"
        file_url = os.path.join(upload_folder, file_name)
        
        # Copy the video to the designated location
        os.replace(video_path, file_url)
        print(f"[INFO] Video saved at: {file_url}")

        # Step 2: Transcribe audio from video
        transcription = transcribe_audio(file_url)
        if not transcription:
            print("[ERROR] Transcription failed.")
            return None

        # Save the transcription to a CSV file
        transcription_path = os.path.join(upload_folder, "transcription.csv")
        with open(transcription_path, "w", encoding="utf-8") as f:
            for line in transcription:
                f.write(f"{line}\n")
        print(f"[INFO] Transcription saved at: {transcription_path}")

        # Step 3: Generate chapter titles from transcription
        chapter_path = generate_chapter_titles(transcription_path, video_id)
        if not chapter_path:
            print("[ERROR] Chapter title generation failed.")
            return None

        # Step 4: Save metadata to PostgreSQL
        metadata = {
            "video_id": video_id,
            "user_id": user_id,
            "category": category,
            "status": "processed",
            "file_url": file_url,
            "transcription": transcription,
            "chapter_path": chapter_path
        }
        save_metadata(video_id, metadata)
        print("[INFO] Pipeline completed successfully.")
        return metadata
    except Exception as e:
        print(f"[ERROR] Pipeline processing failed: {str(e)}")
        return None