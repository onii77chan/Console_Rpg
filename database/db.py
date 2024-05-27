import sqlite3
from database.db_requests import (
    CREATE_TABLES,

)


class Database:
    def __init__(self):
        def connect_and_use_operation(operation):
            with sqlite3.connect('rpg_db.database') as db_connection:
                cursor = db_connection.cursor()
                cursor.execute(operation)
                db_connection.commit()
