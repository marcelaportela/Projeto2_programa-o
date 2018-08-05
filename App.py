from Usuarios import Usuarioprofessor
from Usuarios import Usuarioaluno
from Usuarios import Disciplina
from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
  
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5                      #-------------------------------Crud professor
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.container8 = Frame(master)
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)            #------------------------------------Crud aluno -------------------8 ao 13
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()
        self.container13 = Frame(master)
        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.container14 = Frame(master)
        self.container14["pady"] = 10
        self.container14.pack()
        self.container15 = Frame(master)            #------------------------------------Crud disciplina -------------------14 ao 19
        self.container15["padx"] = 20
        self.container15["pady"] = 5
        self.container15.pack()
        self.container16 = Frame(master)
        self.container16["padx"] = 20
        self.container16["pady"] = 5
        self.container16.pack()
        self.container17 = Frame(master)
        self.container17["padx"] = 20
        self.container17["pady"] = 5
        self.container17.pack()
        self.container18 = Frame(master)
        self.container18["padx"] = 20
        self.container18["pady"] = 5
        self.container18.pack()
        self.container19 = Frame(master)
        self.container19["padx"] = 20
        self.container19["pady"] = 5
        self.container19.pack()
       #-------------------------------------------------------------------------------------------------------CRUD PROFESSOR------------------------------------------------------------
  
        self.titulo = Label(self.container1, text="CRUD PROFESSOR")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lblidprofessor = Label(self.container2, text="idprofessor:", font=self.fonte, width=10)
        self.lblidprofessor.pack(side=LEFT)
  
        self.txtidprofessor = Entry(self.container2)
        self.txtidprofessor["width"] = 10
        self.txtidprofessor["font"] = self.fonte
        self.txtidprofessor.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarprofessor
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblnomeprofessor = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomeprofessor.pack(side=LEFT)
  
        self.txtnomeprofessor = Entry(self.container3)
        self.txtnomeprofessor["width"] = 25
        self.txtnomeprofessor["font"] = self.fonte
        self.txtnomeprofessor.pack(side=LEFT)
  
        self.lblcpfprofessor = Label(self.container4, text="cpf:", font=self.fonte, width=10)
        self.lblcpfprofessor.pack(side=LEFT)
  
        self.txtcpfprofessor = Entry(self.container4)
        self.txtcpfprofessor["width"] = 25
        self.txtcpfprofessor["font"] = self.fonte
        self.txtcpfprofessor.pack(side=LEFT)
  
        self.lbldepartamento= Label(self.container5, text="Departamento:", font=self.fonte, width=12)
        self.lbldepartamento.pack(side=LEFT)
  
        self.txtdepartamento = Entry(self.container5)
        self.txtdepartamento["width"] = 25
        self.txtdepartamento["font"] = self.fonte
        self.txtdepartamento.pack(side=LEFT)
  
  
        self.bntInsert = Button(self.container6, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirprofessor
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.container6, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarprofessor
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.container6, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirprofessor
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


        #----------------------------------------------------------------------------------CRUD ALUNO---------------------------------------------------------------------------------------

        self.titulo = Label(self.container8, text="CRUD ALUNO")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lblidaluno = Label(self.container9, text="idaluno:", font=self.fonte, width=10)
        self.lblidaluno.pack(side=LEFT)
  
        self.txtidaluno = Entry(self.container9)
        self.txtidaluno["width"] = 10
        self.txtidaluno["font"] = self.fonte
        self.txtidaluno.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container9, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscaraluno
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblnome = Label(self.container10, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
  
        self.txtnome = Entry(self.container10)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
  
        self.lblcpf = Label(self.container11, text="cpf:", font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)
  
        self.txtcpf = Entry(self.container11)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)
  
  
        self.bntInsert = Button(self.container12, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inseriraluno
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.container12, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alteraraluno
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.container12, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluiraluno
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container13, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

#------------------------------------------------------------------------------------------CRUD DISCIPLINAS---------------------------------------------------------------------------------

        self.titulo = Label(self.container14, text="CRUD DISCIPLINA")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lbliddisciplina = Label(self.container15, text="iddisciplina:", font=self.fonte, width=10)
        self.lbliddisciplina.pack(side=LEFT)
  
        self.txtiddisciplina = Entry(self.container15)
        self.txtiddisciplina["width"] = 10
        self.txtiddisciplina["font"] = self.fonte
        self.txtiddisciplina.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container15, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscardisciplina
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblnomedisciplina = Label(self.container16, text="Nome:", font=self.fonte, width=10)
        self.lblnomedisciplina.pack(side=LEFT)
  
        self.txtnomedisciplina = Entry(self.container16)
        self.txtnomedisciplina["width"] = 25
        self.txtnomedisciplina["font"] = self.fonte
        self.txtnomedisciplina.pack(side=LEFT)
  
        self.lblcodigodisciplina = Label(self.container17, text="Código da disciplina:", font=self.fonte, width=16)
        self.lblcodigodisciplina.pack(side=LEFT)
  
        self.txtcodigodisciplina = Entry(self.container17)
        self.txtcodigodisciplina["width"] = 25
        self.txtcodigodisciplina["font"] = self.fonte
        self.txtcodigodisciplina.pack(side=LEFT)
  
  
        self.bntInsert = Button(self.container18, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirdisciplina
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.container18, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterardisciplina
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.container18, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirdisciplina
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container19, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
  
  #---------------------------------------------------------------------------------------CRUD PROFESSOR------------------------------------------------------------------------------------
    def inserirprofessor(self):
        user = Usuarioprofessor()
  
        user.nomeprofessor = self.txtnomeprofessor.get()
        user.cpfprofessor = self.txtcpfprofessor.get()
        user.departamento = self.txtdepartamento.get()
  
        self.lblmsg["text"] = user.inserirprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
    def alterarprofessor(self):
        user = Usuarioprofessor()
  
        user.idprofessor = self.txtidprofessor.get()
        user.nomeprofessor = self.txtnomeprofessor.get()
        user.cpfprofessor = self.txtcpfprofessor.get()
        user.departamento = self.txtdepartamento.get()
  
        self.lblmsg["text"] = user.alterarprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
  
    def excluirprofessor(self):
        user = Usuarioprofessor()
  
        user.idprofessor = self.txtidprofessor.get()
  
        self.lblmsg["text"] = user.deletarprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
    def buscarprofessor(self):
        user = Usuarioprofessor()
  
        idprofessor = self.txtidprofessor.get()
  
        self.lblmsg["text"] = user.selecionarprofessor(idprofessor)
  
        self.txtidprofessor.delete(0, END)
        self.txtidprofessor.insert(INSERT, user.idprofessor)
  
        self.txtnomeprofessor.delete(0, END)
        self.txtnomeprofessor.insert(INSERT, user.nomeprofessor)
  
        self.txtcpfprofessor.delete(0, END)
        self.txtcpfprofessor.insert(INSERT,user.cpfprofessor)
  
        self.txtdepartamento.delete(0, END)
        self.txtdepartamento.insert(INSERT, user.departamento)

        #print(user.cpf)
        #print(user.departamento)

  
  #--------------------------------------------------------------------------------------------CRUD ALUNO------------------------------------------------------------------------------------
    def inseriraluno(self):
        user = Usuarioaluno()
  
        user.nome = self.txtnome.get()
        user.cpf = self.txtcpf.get()
  
        self.lblmsg["text"] = user.inseriraluno()
  
        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

  
  
    def alteraraluno(self):
        user = Usuarioaluno()
  
        user.idaluno = self.txtidaluno.get()
        user.nome = self.txtnome.get()
        user.cpf = self.txtcpf.get()
  
        self.lblmsg["text"] = user.alteraraluno()
  
        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
  
  
  
    def excluiraluno(self):
        user = Usuarioaluno()
  
        user.idaluno = self.txtidaluno.get()
  
        self.lblmsg["text"] = user.deletaraluno()
  
        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
  
  
    def buscaraluno(self):
        user = Usuarioaluno()
  
        idaluno = self.txtidaluno.get()
  
        self.lblmsg["text"] = user.selecionaraluno(idaluno)
  
        self.txtidaluno.delete(0, END)
        self.txtidaluno.insert(INSERT, user.idaluno)
  
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
  
        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT,user.cpf)
  
#-----------------------------------------------------------------------------------CRUD DISCIPLINA-------------------------------------------------------------------------------------------

    def inserirdisciplina(self):
        user = Disciplina()
  
        user.nomedisciplina = self.txtnomedisciplina.get()
        user.codigodisciplina = self.txtcodigodisciplina.get()
  
        self.lblmsg["text"] = user.inserirdisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)

  
  
    def alterardisciplina(self):
        user = Disciplina()
  
        user.iddisciplina = self.txtiddisciplina.get()
        user.nomedisciplina = self.txtnomedisciplina.get()
        user.codigodisciplina = self.txtcodigodisciplina.get()
  
        self.lblmsg["text"] = user.alterardisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)
  
  
  
    def excluirdisciplina(self):
        user = Disciplina()
  
        user.iddisciplina = self.txtiddisciplina.get()
  
        self.lblmsg["text"] = user.deletardisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)
  
  
    def buscardisciplina(self):
        user = Disciplina()
  
        iddisciplina = self.txtiddisciplina.get()
  
        self.lblmsg["text"] = user.selecionardisciplina(iddisciplina)
  
        self.txtiddisciplina.delete(0, END)
        self.txtiddisciplina.insert(INSERT, user.iddisciplina)
  
        self.txtnomedisciplina.delete(0, END)
        self.txtnomedisciplina.insert(INSERT, user.nomedisciplina)
  
        self.txtcodigodisciplina.delete(0, END)
        self.txtcodigodisciplina.insert(INSERT,user.codigodisciplina)

  
root = Tk()
Application(root)
root.mainloop()
