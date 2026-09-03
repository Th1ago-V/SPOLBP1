import sqlite3

class Database:
    @staticmethod
    def conectar():
        conn = sqlite3.connect("biblioteca.db")
        # Permite acessar colunas pelo nome (ex: linha['tiulo'])
        conn.row_factory = sqlite3.Row
        return conn
