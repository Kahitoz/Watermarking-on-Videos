from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class UploadData(Base):
    __tablename__ = "upload_data"
    uid = Column(String(50), primary_key=True, unique=True)
    uploadBy = Column(String(500))
    uploadTime = Column(DateTime, default=func.current_timestamp())


class ProcessedData(Base):
    __tablename__ = "processed_data"
    uid = Column(
        String(50), primary_key=True, unique=True
    )
    ProceesedTime = Column(DateTime, default=func.current_timestamp())
