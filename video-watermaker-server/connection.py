import pypyodbc as odbc

DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "192.168.44.132"
DATABASE_NAME = "video-data"
DB_USER = "SA"
DB_PASSWORD = "Kshitiz@25"
DB_SERVER = "192.168.44.132"
DB_DATABASE = "gps_db"
DB_PORT = 1433

# Connection string
connection_string = f"DRIVER={{{DRIVER_NAME}}};SERVER={DB_SERVER},{DB_PORT};DATABASE={DB_DATABASE};UID={DB_USER};PWD={DB_PASSWORD}"

connection = odbc.connect(connection_string)
print(connection)
