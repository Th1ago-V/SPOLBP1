from database import Database

class Usuario:
    @staticmethod
    def criar_tabela():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE,
            senha TEXT)""")
        conn.commit()
        conn.close()

    @staticmethod
    def cadastrar(login, senha):
        try:
            conn = Database.conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (login,senha) VALUES (?, ?)", (login, senha))
            conn.commit()
            conn.close
            return True
        except Exception:
            return False
        
    @staticmethod
    def autenticar(login, senha):
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha=?", (login, senha))
        usuario = cursor.fetchone()
        conn.close()
        return usuario