import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DRIVER_NAME = "SQL Server"
SERVER_NAME = "192.168.44.132"
DB_USER = "SA"
DB_PASSWORD = "Kshitiz@25"
DB_SERVER = "192.168.44.132"
DB_DATABASE = "video-data"
DB_PORT = 1433

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_SERVER},{DB_PORT};DATABASE={DB_DATABASE};UID={DB_USER};PWD={DB_PASSWORD}"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

Session = sessionmaker(bind=engine)
