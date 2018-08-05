#importando módulo do SQlite
import sqlite3

class Bancoprofessores():
  
    def __init__(self):
        self.conexao = sqlite3.connect('bancoprofessores.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists professores (
                     idprofessor integer primary key autoincrement ,
                     nomeprofessor text,
                     cpfprofessor text,
                     departamento text)""")
        self.conexao.commit()
        c.close()
