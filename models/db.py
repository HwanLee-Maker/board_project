import pymysql
from config import Config

def get_db():
    return pymysql.connect(**Config.DB_CONFIG)