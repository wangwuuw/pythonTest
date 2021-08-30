import pymysql

db_config = {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'root',
                'password': 'root',
                'db': 'ui',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
def config_init():
    return