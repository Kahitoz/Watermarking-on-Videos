from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UploadData(Base):
    __tablename__ = "upload_data"
    uid = Column(String(50), primary_key=True, unique=True)
    filename = Column(String(500))
    uploadTime = Column(DateTime, default=func.current_timestamp())
