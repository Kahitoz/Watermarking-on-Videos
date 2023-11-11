from fastapi import FastAPI, File, UploadFile, HTTPException, Query, Form, Path
from fastapi.responses import JSONResponse, StreamingResponse
from operations import insert_data, insert_processed_data
from processing import add_watermark

import shutil
import os
import uuid

app = FastAPI()

UPLOADS_DIR = os.path.join("video_storage", "Uploads")


@app.post("/upload-video/")
async def upload_video(
    file: UploadFile = File(...),
    watermark_position: int = Query(..., description="Watermark position (1 to 8)"),
    username: str = Form(..., description="Username"),
):
    try:
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        unique_id = str(uuid.uuid4())

        # Combine unique ID and sanitized filename
        filename = f"{unique_id}"

        file_path = os.path.join(UPLOADS_DIR, filename)

        print(file_path)

        file_path = file_path.replace("\\", "\\\\")

        with open(file_path, "wb") as video_file:
            shutil.copyfileobj(file.file, video_file)

        try:
            insert_data(unique_id, username)
            pass
        except Exception as e:
            print("Some error occurred while saving it in the database", e)

        # Apply watermark to the uploaded video
        add_watermark(unique_id, file_path, position_case=watermark_position)

        return JSONResponse(
            content={
                "message": "File uploaded successfully",
                "file_path": file_path,
                "watermark_position": watermark_position,
                "username": username,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


PROCESSED_DIR = os.path.join("video_storage", "Processed")
print(PROCESSED_DIR)


@app.get("/get-processed-video/{uid}")
async def get_processed_video(
    uid: str = Path(..., description="Unique ID of the video")
):
    try:
        processed_filename = f"{uid}.mp4"
        print(processed_filename)
        processed_filepath = os.path.join(PROCESSED_DIR, processed_filename)

        if not os.path.exists(processed_filepath):
            raise HTTPException(status_code=404, detail="Processed video not found")
        return StreamingResponse(
            open(processed_filepath, "rb"), media_type="application/octet-stream"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
