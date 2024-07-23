import sqlite3


class DB:

    def __init__(self, db_url):
        self.db_url = db_url

    def add_values_to_db(self, data: list, table_name: str):
        pass
