from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from operations import insert_data, insert_processed_data
from processing import add_watermark

import shutil
import os
import uuid

app = FastAPI()

UPLOADS_DIR = os.path.join("video_storage", "Uploads")

global_uid = []


@app.post("/upload-video/")
async def upload_video(file: UploadFile = File(...)):
    try:
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Replace spaces in the filename
        sanitized_filename = file.filename.replace(" ", "_")

        # Construct the file path using double slashes
        file_path = os.path.join(UPLOADS_DIR, sanitized_filename)

        with open(file_path, "wb") as video_file:
            shutil.copyfileobj(file.file, video_file)

        unique_id = str(uuid.uuid4())
        filename = sanitized_filename  # Use the sanitized filename

        try:
            insert_data(unique_id, filename)
        except Exception as e:
            print("Some error occurred while saving it in the database", e)

        return JSONResponse(
            content={"message": "File uploaded successfully", "file_path": file_path}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
