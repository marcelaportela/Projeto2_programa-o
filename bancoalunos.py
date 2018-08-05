import sqlite3

class Bancoalunos():
  
    def __init__(self):
        self.conexao = sqlite3.connect('bancoalunos.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists alunos (
                     idaluno integer primary key autoincrement ,
                     nome text,
                     cpf text)""")
        self.conexao.commit()
        c.close()
