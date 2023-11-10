from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse
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
):
    try:
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Replace spaces, hyphens, and dots in the filename
        sanitized_filename = (
            file.filename.replace(" ", "").replace("-", "").replace(".", "")
        )

        # Construct the file path using double slashes
        file_path = os.path.join(UPLOADS_DIR, sanitized_filename)

        print(file_path)

        # Replace backslashes with double backslashes

        with open(file_path, "wb") as video_file:
            shutil.copyfileobj(file.file, video_file)

        unique_id = str(uuid.uuid4())
        filename = sanitized_filename  # Use the sanitized filename

        try:
            insert_data(unique_id, filename)  # Assuming this function exists
            pass
        except Exception as e:
            print("Some error occurred while saving it in the database", e)

        file_path = file_path.replace("\\", "\\\\")

        # Apply watermark to the uploaded video
        add_watermark(unique_id, file_path, position_case=watermark_position)

        return JSONResponse(
            content={
                "message": "File uploaded successfully",
                "file_path": file_path,
                "watermark_position": watermark_position,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
