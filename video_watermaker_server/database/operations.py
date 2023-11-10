from sqlalchemy.orm import Session
from models import UploadData, ProcessedData
from db import Session as DbSession, engine
from models import Base


# Database operations functions
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


def add_data_processed(db: Session, uid:str, filename: str):
    new_upload = ProcessedData(uid = uid, filename = filename)
    db.add(new_upload)
    db.commit()
    db.refresh(new_upload)
    return new_upload


Base.metadata.create_all(bind=engine)


# methods to be used for api and other files
def insert_data(uid, filename):
    with DbSession() as db:
        new_upload = add_data(db=db, uid=uid, filename=filename)
        print(
            f"Data added successfully with UID: {new_upload.uid}, Filename: {new_upload.filename}"
        )


def insert_processed_data(uid, filename):
    with DbSession() as db:
        new_upload = add_data_processed(db=db, uid=uid, filename=filename)
        print(
            f"Processed Data added successfully with UID: {new_upload.uid}, Filename: {new_upload.filename}"
        )


def show_all_data_upload_table():
    with DbSession() as db:
        print_all_data(db=db)


# show_all_data_upload_table()
