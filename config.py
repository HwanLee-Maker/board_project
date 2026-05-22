import pymysql

class Config:
    SECRET_KEY = "dev_secret_key"

    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "1234",
        "database": "board_db",
        "cursorclass": pymysql.cursors.DictCursor   
    }