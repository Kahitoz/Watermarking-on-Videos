from sqlalchemy.orm import Session
from models import UploadData
from db import Session as DbSession, engine
from models import Base


def add_data(db: Session, uid: str, filename: str):
    new_upload = UploadData(uid=uid, filename=filename)
    db.add(new_upload)
    db.commit()
    db.refresh(new_upload)
    return new_upload


def print_all_data(db: Session):
    all_data = db.query(UploadData).all()
    print("All data in 'upload_data' table:")
    for data in all_data:
        print(
            f"UID: {data.uid}, Filename: {data.filename}, Upload Time: {data.uploadTime}"
        )


Base.metadata.create_all(bind=engine)

with DbSession() as db:
    new_upload = add_data(db=db, uid="123456", filename="example_file.mp4")
    print(
        f"Data added successfully with UID: {new_upload.uid}, Filename: {new_upload.filename}"
    )
    print_all_data(db=db)
