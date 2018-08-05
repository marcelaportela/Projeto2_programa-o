import sqlite3

class Bancodisciplinas():
  
    def __init__(self):
        self.conexao = sqlite3.connect('bancodisciplinas.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists disciplinas (
                     iddisciplina integer primary key autoincrement ,
                     nomedisciplina text,
                     codigodisciplina text)""")
        self.conexao.commit()
        c.close()
