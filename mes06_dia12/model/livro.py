from database import Database
import pandas as pd
import os

class Livro:
    @staticmethod
    def criar():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor1 TEXT, autor2 TEXT, autor3 TEXT, isbn TEXT, assunto TEXT, edicao TEXT, editora TEXT, ano INTEGER
        )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def inserir(titulo, autor1, autor2, autor3, isbn, assunto, edicao, editora, ano):
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO livros (titulo, autor1, autor2, autor3, isbn, assunto, edicao, editora, ano)
        VALUES (?,?,?,?,?,?,?,?,?)
        """, (titulo, autor1, autor2, autor3, isbn, assunto, edicao, editora, ano))
        conn.commit()
        conn.close()

    @staticmethod
    def consultar():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    @staticmethod
    def excluir(id_livro):
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))
        conn.commit()
        conn.close()

    @staticmethod
    def exportar():
        conn = Database.conectar()

        #Necessário ler usando uma query crua para o pandas converter de volta para dataframe
        import sqlite3
        conn_pandas = sqlite3.connect("biblioteca.db")
        df = pd.read_sql('SELECT * FROM livros', conn_pandas)

        #Garante o salvamento na pasta do app
        caminho = os.path.join(os.getcwd(), "livros.xlsx")
        df.to_excel(caminho, index=False)
        conn_pandas.close()
        return caminho
    