from bancoprofessores import Bancoprofessores
from bancoalunos import Bancoalunos
from bancodisciplinas import Bancodisciplinas
from bancoturmas import Bancoturmas

  
class Usuarioprofessor(object):
  
  
    def __init__(self, idprofessor = 0, nomeprofessor = "nao cadastrado", cpfprofessor = "nao cadastrado", departamento = "nao cadastrado"):
        self.info = {}
        self.idprofessor = idprofessor
        self.nomeprofessor = nomeprofessor
        self.cpfprofessor = cpfprofessor
        self.departamento = departamento
  
  
    def inserirprofessor(self):
  
        bancoprofessores = Bancoprofessores()
        try:
  
            c = bancoprofessores.conexao.cursor()
  
            c.execute("insert into professores (nomeprofessor, cpfprofessor, departamento) values ('" + self.nomeprofessor + "', '" + self.cpfprofessor + "', '" + self.departamento+ "' )")
  
            bancoprofessores.conexao.commit()
            c.close()
  
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
  
    def alterarprofessor(self):
  
        bancoprofessores = Bancoprofessores()
        try:
  
            c = bancoprofessores.conexao.cursor()
  
            c.execute("update professores set nomeprofessor = '" + self.nomeprofessor + "', cpfprofessor = '" + self.cpfprofessor + "', departamento = '" + self.departamento + "' where idprofessor = " + self.idprofessor + " ")
  
            bancoprofessores.conexao.commit()  
            c.close()
  
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
  
    def deletarprofessor(self):
  
        bancoprofessores = Bancoprofessores()
        try:
  
            c = bancoprofessores.conexao.cursor()
  
            c.execute("delete from professores where idprofessor = " + self.idprofessor + " ")
  
            bancoprofessores.conexao.commit()
            c.close()
  
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
  
    def selecionarprofessor(self, idprofessor):
        bancoprofessores = Bancoprofessores()
        try:
  
            c = bancoprofessores.conexao.cursor()
  
            c.execute("select * from professores where idprofessor = " + idprofessor + "  ")
  
            for linha in c:
                self.idprofessor = linha[0]
                self.nomeprofessor = linha[1]
                self.cpfprofessor = linha[2]
                self.departamento = linha[3]
  
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"

#----------------------------------------------------------------------------------------Crud Alunos--------------------------------------------------------------------------------------------

class Usuarioaluno(object):
  
  
    def __init__(self, idaluno = 0, nome = "nao cadastrado", cpf = "nao cadastrado"):
        self.info = {}
        self.idaluno = idaluno
        self.nome = nome
        self.cpf = cpf
  
  
    def inseriraluno(self):
  
        bancoalunos = Bancoalunos()
        try:
  
            c = bancoalunos.conexao.cursor()
  
            c.execute("insert into alunos (nome, cpf) values ('" + self.nome + "', '" + self.cpf +"' )")
  
            bancoalunos.conexao.commit()
            c.close()
  
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
  
    def alteraraluno(self):
  
        bancoalunos = Bancoalunos()
        try:
  
            c = bancoalunos.conexao.cursor()
  
            c.execute("update alunos set nome = '" + self.nome + "', cpf = '" + self.cpf + "' where idprofessor = " + self.idaluno + " ")
  
            bancoalunos.conexao.commit()  
            c.close()
  
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
  
    def deletaraluno(self):
  
        bancoalunos = Bancoalunos()
        try:
  
            c = bancoalunos.conexao.cursor()
  
            c.execute("delete from alunos where idaluno = " + self.idaluno + " ")
  
            bancoalunos.conexao.commit()
            c.close()
  
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
  
    def selecionaraluno(self, idaluno):
        bancoalunos = Bancoalunos()
        try:
  
            c = bancoalunos.conexao.cursor()
  
            c.execute("select * from alunos where idaluno = " + idaluno + "  ")
  
            for linha in c:
                self.idaluno = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
  
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
#----------------------------------------------------------------------------------------------------CRUD Disciplinas-----------------------------------------------------------------------

class Disciplina(object):
  
  
    def __init__(self, iddisciplina = 0, nomedisciplina = "nao cadastrado", codigodisciplina = "nao cadastrado"):
        self.info = {}
        self.iddisciplina = iddisciplina
        self.nomedisciplina = nomedisciplina
        self.codigodisciplina = codigodisciplina
  
  
    def inserirdisciplina(self):
  
        bancodisciplinas = Bancodisciplinas()
        try:
  
            c = bancodisciplinas.conexao.cursor()
  
            c.execute("insert into disciplinas (nomedisciplina, codigodisciplina) values ('" + self.nomedisciplina + "', '" + self.codigodisciplina +"' )")
  
            bancodisciplinas.conexao.commit()
            c.close()
  
            return "Disciplina cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da disciplina"
  
    def alterardisciplina(self):
  
        bancodisciplinas = Bancodisciplinas()
        try:
  
            c = bancodisciplinas.conexao.cursor()
  
            c.execute("update disciplinas set nomedisciplina = '" + self.nomedisciplina + "', codigodisciplina = '" + self.codigodisciplina + "' where iddisciplina = " + self.iddisciplina + " ")
  
            bancodisciplinas.conexao.commit()  
            c.close()
  
            return "Disciplina atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da disciplina"
  
    def deletardisciplina(self):
  
        bancodisciplinas = Bancodisciplinas()
        try:
  
            c = bancodisciplinas.conexao.cursor()
  
            c.execute("delete from disciplinas where iddisciplina = " + self.iddisciplina + " ")
  
            bancodisciplinas.conexao.commit()
            c.close()
  
            return "Disciplina excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da disciplina"
  
    def selecionardisciplina(self, iddisciplina):
        bancodisciplinas = Bancodisciplinas()
        try:
  
            c = bancodisciplinas.conexao.cursor()
  
            c.execute("select * from disciplinas where iddisciplina = " + iddisciplina + "  ")
  
            for linha in c:
                self.iddisciplina = linha[0]
                self.nomedisciplina = linha[1]
                self.codigodisciplina = linha[2]
  
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da disciplina"
#----------------------------------------------------------------------------------------------CRUD TURMAS-----------------------------------------------------------------------------------
class Turma(object):
  
  
    def __init__(self, idturma = 0, codigoturma = "nao cadastrado", periodo = "nao cadastrado", codigodisciplina= "nao cadastrado", cpfprofessor= "nao cadastrado", lista_cpf_alunos = "nao cadastrado"):
        self.info = {}
        self.idturma = idturma
        self.codigoturma = codigoturma
        self.periodo = periodo
        self.codigodisciplina = codigodisciplina
        self.cpfprofessor = cpfprofessor
        self.lista_cpf_alunos = lista_cpf_alunos

                     #codigoturma text,
                     #periodo text,
                     #codigodisciplina text,
                     #cpfprofessor  text,
                     #lista_cpf_alunos text)""
  
  
    def inserirturma(self):
  
        bancoturmas = Bancoturmas()
        try:
  
            c = bancoturmas.conexao.cursor()
  
            c.execute("insert into turmas (codigoturma, periodo, codigodisciplina, cpfprofessor, lista_cpf_alunos) values ('" + self.codigoturma + "', '" + self.periodo + "', '" + self.codigodisciplina + "', '" + self.cpfprofessor + "', '" + self.lista_cpf_alunos +"' )")
  
            bancoturmas.conexao.commit()
            c.close()
  
            return "Turma cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da turma"
  
    def alterarturma(self):
  
        bancoturmas = Bancoturmas()
        try:
  
            c = bancoturmas.conexao.cursor()
  
            c.execute("update turmas set codigoturma = '" + self.codigoturma + "', periodo = '" + self.periodo + "', codigodisciplina = '" + self.codigodisciplina + "', cpfprofessor = '" + self.cpfprofessor + "', lista_cpf_alunos = '" + self.lista_cpf_alunos + "' where idturma = " + self.idturma + " ")
  
            bancoturma.conexao.commit()  
            c.close()
  
            return "Turma atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da turma"
  
    def deletarturma(self):
  
        bancoturmas = Bancoturmas()
        try:
  
            c = bancoturmas.conexao.cursor()
  
            c.execute("delete from turmas where idturma = " + self.idturma + " ")
  
            bancoturmas.conexao.commit()
            c.close()
  
            return "Turma excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da turma"
  
    def selecionarturma(self, idturma):
        bancoturmas = Bancoturmas()
        try:
  
            c = bancoturmas.conexao.cursor()
  
            c.execute("select * from turmas where idturma = " + idturma + "  ")
  
            for linha in c:
                self.idturma = linha[0]
                self.codigoturma = linha[1]
                self.periodo = linha[2]
                self.codigodisciplina = linha[3]
                self.cpfprofessor[4]
                self.lista_cpf_alunos[5]
                     #codigoturma text,
                     #periodo text,
                     #codigodisciplina text,
                     #cpfprofessor  text,
                     #lista_cpf_alunos text)""
            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da turma"
