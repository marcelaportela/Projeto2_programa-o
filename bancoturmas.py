import sqlite3

class Bancoturmas():
  
    def __init__(self):
        self.conexao = sqlite3.connect('bancoturmas.db')
        self.createTable()
  
    def createTable(self):
        c = self.conexao.cursor()
  
        c.execute("""create table if not exists turmas (
                     idturma integer primary key autoincrement ,
                     codigoturma text,
                     periodo text,
                     turmacodigodisciplina text,
                     turmacpfprofessor  text,
                     lista_cpf_alunos text)""")
        self.conexao.commit()
        c.close()
