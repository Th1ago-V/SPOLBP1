from model.database import Database
import pandas as pd

def exportar():
    conn = Database.conectar()

    df = pd.read_sql("SELECT * FROM produtos",
    conn)

    df.to_excel(
    "produtos.xlsx", 
    index=False)

    print("Planilha criada")

class Produto:
    @staticmethod
    def criar():
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        modelo TEXT,
        fabricante TEXT,
        preco TEXT)
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def inserir(nome,modelo,fabricante,preco):
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO produtos(
        nome,
        modelo,
        fabricante,
        preco)
        VALUES(?,?,?,?)""",(nome,modelo,fabricante,preco))

        conn.commit()
        conn.close()

    @staticmethod
    def consultar():
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM produtos"
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    @staticmethod
    def excluir(id_produto):
        conn = Database.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM produtos WHERE id=?",
            (id_produto,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def exportar():
        try:
            conn = Database.conectar()
            df = pd.read_sql("SELECT * FROM produtos",
            conn)

            df.to_excel(
                "produtos.xlsx", 
                index=False)

            conn.close()
            print("Exportação concluida")

        except ModuloNotFoundError:
            print("Instale: pip install openpyxl")
            
        except Exeception as erro:
            print(f"Erro:{erro}")