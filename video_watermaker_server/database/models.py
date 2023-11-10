from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class UploadData(Base):
    __tablename__ = "upload_data"
    uid = Column(String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    filename = Column(String(500))
    uploadTime = Column(DateTime, default=func.current_timestamp())


class ProcessedData(Base):
    __tablename__ = "processed_data"
    uid = uid = Column(
        String(50), primary_key=True, default=str(uuid.uuid4()), unique=True
    )
    filename = Column(String(500))
    uploadTime = Column(DateTime, default=func.current_timestamp())
