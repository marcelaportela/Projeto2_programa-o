from Usuarios import Usuarioprofessor
from Usuarios import Usuarioaluno
from Usuarios import Disciplina
from Usuarios import Turma
from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
  
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.place(x = 100, y = 10, width=120, height=50)
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.place(x = 30, y = 50, width=300, height=70)
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5                      #-------------------------------Crud professor
        self.container3.place(x = 30, y = 100, width=300, height=70)
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.place(x = 30, y = 150, width=300, height=70)
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.place(x = 30, y = 200, width=300, height=70)
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.place(x = 30, y = 250, width=300, height=70)
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.place(x = 30, y = 300, width=300, height=70)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.container8 = Frame(master)
        self.container8["pady"] = 10
        self.container8.place(x = 30, y = 400, width=120, height=50)
        self.container9 = Frame(master)            #------------------------------------Crud aluno -------------------8 ao 13
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.place(x = 30, y = 450, width=300, height=70)
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.place(x = 30, y = 500, width=300, height=70)
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.place(x = 30, y = 550, width=300, height=70)
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.place(x = 30, y = 600, width=300, height=70)
        self.container13 = Frame(master)
        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.place(x = 30, y = 650, width=300, height=70)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.container14 = Frame(master)
        self.container14["pady"] = 10
        self.container14.place(x = 470, y = 10, width=120, height=50)
        self.container15 = Frame(master)            #------------------------------------Crud disciplina -------------------14 ao 19
        self.container15["padx"] = 20
        self.container15["pady"] = 5
        self.container15.place(x = 400, y = 50, width=300, height=70)
        self.container16 = Frame(master)
        self.container16["padx"] = 20
        self.container16["pady"] = 5
        self.container16.place(x = 400, y = 100, width=300, height=70)
        self.container17 = Frame(master)
        self.container17["padx"] = 20
        self.container17["pady"] = 5
        self.container17.place(x = 400, y = 150, width=300, height=70)
        self.container18 = Frame(master)
        self.container18["padx"] = 20
        self.container18["pady"] = 5
        self.container18.place(x = 400, y = 200, width=300, height=70)
        self.container19 = Frame(master)
        self.container19["padx"] = 20
        self.container19["pady"] = 5
        self.container19.place(x = 400, y = 250, width=300, height=70)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.container20 = Frame(master)   # texto de cima
        self.container20["pady"] = 10
        self.container20.place(x = 400, y = 350, width=300, height=70)
                                                    # texto de cima, id + botao buscar, nome, codigo, 3 botoes e texto de baixo
        self.container21 = Frame(master)
                                                    #------------------------------------Crud turma -------------------20 ao 28
                                                    #TEXTO DE CIMA 20
                                                    #ID+BOTAO BUSCAR 21
                                                    #codigoturma text,  22
                                                    #periodo text, 23
                                                    #turmacodigodisciplina text, 24
                                                    #turmacpfprofessor  text, 25
                                                    #lista_cpf_alunos text)"" 26
                                                    #3botoes 27
                                                    #texto de baixo 28
        
        self.container21["padx"] = 20 #id + botao buscar
        self.container21["pady"] = 5
        self.container21.place(x = 400, y = 400, width=300, height=70)
        self.container22 = Frame(master) #codigoturma
        self.container22["padx"] = 20
        self.container22["pady"] = 5
        self.container22.place(x = 400, y = 450, width=300, height=70)
        self.container23 = Frame(master) #periodo
        self.container23["padx"] = 20
        self.container23["pady"] = 5
        self.container23.place(x = 400, y = 500, width=300, height=70)
        self.container24 = Frame(master) #codigodisciplina
        self.container24["padx"] = 20
        self.container24["pady"] = 5
        self.container24.place(x = 400, y = 550, width=300, height=70)

        self.container25 = Frame(master) #cpfprofessor
        self.container25["padx"] = 40
        self.container25["pady"] = 10
        self.container25.place(x = 400, y = 600, width=500, height=70)
        self.container26 = Frame(master)  #lista_cpf_alunos
        self.container26["padx"] = 20
        self.container26["pady"] = 5
        self.container26.place(x = 400, y = 650, width=400, height=70)
        
        self.container27 = Frame(master) #3 BOTOES
        self.container27["padx"] = 20
        self.container27["pady"] = 5
        self.container27.place(x = 400, y = 700, width=300, height=70)

        self.container28 = Frame(master) #TEXTO DE BAIXO
        self.container28["padx"] = 20
        self.container28["pady"] = 5
        self.container28.place(x = 400, y = 750, width=300, height=70)

        
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
#-----------------------------------------------------------------------------------------CRUD TURMA----------------------------------------------------------------------------------------

        #------------------------------------Crud turma -------------------20 ao 28
                                                    #TEXTO DE CIMA 20
                                                    #ID+BOTAO BUSCAR 21
                                                    #codigoturma text,  22
                                                    #periodo text, 23
                                                    #codigodisciplina text, 24
                                                    #cpfprofessor  text, 25
                                                    #lista_cpf_alunos text)"" 26
                                                    #3botoes 27
                                                    #texto de baixo 28
        
        self.titulo = Label(self.container20, text="CRUD TURMA")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lblidturma = Label(self.container21, text="idturma:", font=self.fonte, width=10)
        self.lblidturma.pack(side=LEFT)
  
        self.txtidturma = Entry(self.container21)
        self.txtidturma["width"] = 10
        self.txtidturma["font"] = self.fonte
        self.txtidturma.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container21, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarturma
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblcodigoturma = Label(self.container22, text="Código da turma:", font=self.fonte, width=16)
        self.lblcodigoturma.pack(side=LEFT)
  
        self.txtcodigoturma = Entry(self.container22)
        self.txtcodigoturma["width"] = 25
        self.txtcodigoturma["font"] = self.fonte
        self.txtcodigoturma.pack(side=LEFT)
  
        self.lblperiodo = Label(self.container23, text="Período:", font=self.fonte, width=16)
        self.lblperiodo.pack(side=LEFT)
  
        self.txtperiodo = Entry(self.container23)
        self.txtperiodo["width"] = 25
        self.txtperiodo["font"] = self.fonte
        self.txtperiodo.pack(side=LEFT)

        self.lblturmacodigodisciplina = Label(self.container24, text="Código da disciplina:", font=self.fonte, width=16)
        self.lblturmacodigodisciplina.pack(side=LEFT)
  
        self.txtturmacodigodisciplina = Entry(self.container24)
        self.txtturmacodigodisciplina["width"] = 25
        self.txtturmacodigodisciplina["font"] = self.fonte
        self.txtturmacodigodisciplina.pack(side=LEFT)

                #------------------------------------Crud turma -------------------20 ao 28
                                                    #TEXTO DE CIMA 20
                                                    #ID+BOTAO BUSCAR 21
                                                    #codigoturma text,  22
                                                    #periodo text, 23
                                                    #codigodisciplina text, 24
                                                    #cpfprofessor  text, 25
                                                    #lista_cpf_alunos text)"" 26
                                                    #3botoes 27
                                                    #texto de baixo 28

        self.lblturmacpfprofessor = Label(self.container25, text="cpf do professor:", font=self.fonte, width=20)
        self.lblturmacpfprofessor.pack(side=LEFT)
  
        self.txtturmacpfprofessor = Entry(self.container25)
        self.txtturmacpfprofessor["width"] = 25
        self.txtturmacpfprofessor["font"] = self.fonte
        self.txtturmacpfprofessor.pack(side=LEFT)

        self.lbllista_cpf_alunos = Label(self.container26, text="cpf do aluno:", font=self.fonte, width=16)
        self.lbllista_cpf_alunos.pack(side=LEFT)
  
        self.txtlista_cpf_alunos = Entry(self.container26)
        self.txtlista_cpf_alunos["width"] = 25
        self.txtlista_cpf_alunos["font"] = self.fonte
        self.txtlista_cpf_alunos.pack(side=LEFT)
  
  
        self.bntInsert = Button(self.container27, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirturma
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.container27, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarturma
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.container27, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirturma
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container28, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
  
  #---------------------------------------------------------------------------------------CRUD PROFESSOR------------------------------------------------------------------------------------
    def inserirprofessor(self):
        user1 = Usuarioprofessor()
  
        user1.nomeprofessor = self.txtnomeprofessor.get()
        user1.cpfprofessor = self.txtcpfprofessor.get()
        user1.departamento = self.txtdepartamento.get()
  
        self.lblmsg["text"] = user1.inserirprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
    def alterarprofessor(self):
        user1 = Usuarioprofessor()
  
        user1.idprofessor = self.txtidprofessor.get()
        user1.nomeprofessor = self.txtnomeprofessor.get()
        user1.cpfprofessor = self.txtcpfprofessor.get()
        user1.departamento = self.txtdepartamento.get()
  
        self.lblmsg["text"] = user1.alterarprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
  
    def excluirprofessor(self):
        user1 = Usuarioprofessor()
  
        user1.idprofessor = self.txtidprofessor.get()
  
        self.lblmsg["text"] = user1.deletarprofessor()
  
        self.txtidprofessor.delete(0, END)
        self.txtnomeprofessor.delete(0, END)
        self.txtcpfprofessor.delete(0, END)
        self.txtdepartamento.delete(0, END)
  
  
    def buscarprofessor(self):
        user1 = Usuarioprofessor()
  
        idprofessor = self.txtidprofessor.get()
  
        self.lblmsg["text"] = user1.selecionarprofessor(idprofessor)
  
        self.txtidprofessor.delete(0, END)
        self.txtidprofessor.insert(INSERT, user1.idprofessor)
  
        self.txtnomeprofessor.delete(0, END)
        self.txtnomeprofessor.insert(INSERT, user1.nomeprofessor)
  
        self.txtcpfprofessor.delete(0, END)
        self.txtcpfprofessor.insert(INSERT,user1.cpfprofessor)
  
        self.txtdepartamento.delete(0, END)
        self.txtdepartamento.insert(INSERT, user1.departamento)

        #print(user.cpf)
        #print(user.departamento)

  
  #--------------------------------------------------------------------------------------------CRUD ALUNO------------------------------------------------------------------------------------
    def inseriraluno(self):
        user2 = Usuarioaluno()
  
        user2.nome = self.txtnome.get()
        user2.cpf = self.txtcpf.get()

        #print(user2.nome)
        #print(user2.cpf)
  
        self.lblmsg["text"] = user2.inseriraluno()
  
        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

  
  
    def alteraraluno(self):
        user2 = Usuarioaluno()
  
        user2.idaluno = self.txtidaluno.get()
        user2.nome = self.txtnome.get()
        user2.cpf = self.txtcpf.get()
  
        self.lblmsg["text"] = user2.alteraraluno()
  
        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
  
  
  
    def excluiraluno(self):
        user2 = Usuarioaluno()
  
        user2.idaluno = self.txtidaluno.get()
  
        self.lblmsg["text"] = user2.deletaraluno()
  
        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
  
  
    def buscaraluno(self):
        user2 = Usuarioaluno()
  
        idaluno = self.txtidaluno.get()
  
        self.lblmsg["text"] = user2.selecionaraluno(idaluno)
  
        self.txtidaluno.delete(0, END)
        self.txtidaluno.insert(INSERT, user2.idaluno)
  
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user2.nome)
  
        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT,user2.cpf)
  
#-----------------------------------------------------------------------------------CRUD DISCIPLINA-------------------------------------------------------------------------------------------

    def inserirdisciplina(self):
        user3 = Disciplina()
  
        user3.nomedisciplina = self.txtnomedisciplina.get()
        user3.codigodisciplina = self.txtcodigodisciplina.get()
  
        self.lblmsg["text"] = user3.inserirdisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)

  
  
    def alterardisciplina(self):
        user3 = Disciplina()
  
        user3.iddisciplina = self.txtiddisciplina.get()
        user3.nomedisciplina = self.txtnomedisciplina.get()
        user3.codigodisciplina = self.txtcodigodisciplina.get()
  
        self.lblmsg["text"] = user3.alterardisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)
  
  
  
    def excluirdisciplina(self):
        user3 = Disciplina()
  
        user3.iddisciplina = self.txtiddisciplina.get()
  
        self.lblmsg["text"] = user3.deletardisciplina()
  
        self.txtiddisciplina.delete(0, END)
        self.txtnomedisciplina.delete(0, END)
        self.txtcodigodisciplina.delete(0, END)
  
  
    def buscardisciplina(self):
        user3 = Disciplina()
  
        iddisciplina = self.txtiddisciplina.get()
  
        self.lblmsg["text"] = user3.selecionardisciplina(iddisciplina)
  
        self.txtiddisciplina.delete(0, END)
        self.txtiddisciplina.insert(INSERT, user3.iddisciplina)
  
        self.txtnomedisciplina.delete(0, END)
        self.txtnomedisciplina.insert(INSERT, user3.nomedisciplina)
  
        self.txtcodigodisciplina.delete(0, END)
        self.txtcodigodisciplina.insert(INSERT,user3.codigodisciplina)

#-------------------------------------------------------------------------------------------CRUD TURMAS-------------------------------------------------------------------------------------

#------------------------------------Crud turma -------------------20 ao 28
                                                    #TEXTO DE CIMA 20
                                                    #ID+BOTAO BUSCAR 21
                                                    #codigoturma text,  22
                                                    #periodo text, 23
                                                    #codigodisciplina text, 24
                                                    #cpfprofessor  text, 25
                                                    #lista_cpf_alunos text)"" 26
                                                    #3botoes 27
                                                    #texto de baixo 28

    def inserirturma(self):
        user4 = Turma()
  
        user4.codigoturma = self.txtcodigoturma.get()
        user4.periodo = self.txtperiodo.get()
        user4.turmacodigodisciplina = self.txtturmacodigodisciplina.get()
        user4.turmacpfprofessor = self.txtturmacpfprofessor.get()
        user4.lista_cpf_alunos = self.txtlista_cpf_alunos.get()

        print(user4.codigoturma)
        print(user4.periodo)
        print(user4.turmacodigodisciplina)
        print(user4.turmacpfprofessor)
        print(user4.lista_cpf_alunos)
        
  
        self.lblmsg["text"] = user4.inserturma()
  
        self.txtidturma.delete(0, END)
        self.txtcodigoturma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtturmacodigodisciplina.delete(0, END)
        self.txtturmacpfprofessor.delete(0, END)
        self.txtlista_cpf_alunos.delete(0, END)

  
  
    def alterarturma(self):
        user4 = Turma()
  
        user4.idturma = self.txtiddisciplina.get()
        user4.codigoturma = self.txtcodigoturma.get()
        user4.periodo = self.txtperiodo.get()
        user4.turmacodigodisciplina = self.txtturmacodigodisciplina.get()
        user4.turmacpfprofessor = self.txtturmacpfprofessor.get()
        user4.lista_cpf_alunos = self.txtlista_cpf_alunos.get()
  
        self.lblmsg["text"] = user4.alterturma()
  
        self.txtidturma.delete(0, END)
        self.txtcodigoturma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtturmacodigodisciplina.delete(0, END)
        self.txtturmacpfprofessor.delete(0, END)
        self.txtlista_cpf_alunos.delete(0, END)
  
  
  
    def excluirturma(self):
        user4 = Turma()
  
        user4.idturma = self.txtidturma.get()
  
        self.lblmsg["text"] = user4.deletarturma()
  
        self.txtidturma.delete(0, END)
        self.txtcodigoturma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtturmacodigodisciplina.delete(0, END)
        self.txtturmacpfprofessor.delete(0, END)
        self.txtlista_cpf_alunos.delete(0, END)
  
  
    def buscarturma(self):
        user4 = Turma()
  
        idturma = self.txtidturma.get()
  
        self.lblmsg["text"] = user4.selecionarturma(idturma)
  
        self.txtidturma.delete(0, END)
        self.txtidturma.insert(INSERT, user4.idturma)
  
        self.txtcodigoturma.delete(0, END)
        self.txtcodigoturma.insert(INSERT, user4.codigoturma)
  
        self.txtperiodo.delete(0, END)
        self.txtperiodo.insert(INSERT,user4.periodo)

        self.txtturmacodigodisciplina.delete(0, END)
        self.txtturmacodigodisciplina.insert(INSERT, user4.turmacodigodisciplina)
  
        self.txtturmacpfprofessor.delete(0, END)
        self.txtturmacpfprofessor.insert(INSERT,user4.turmacpfprofessor)

        self.txtlista_cpf_alunos.delete(0, END)
        self.txtlista_cpf_alunos.insert(INSERT,user4.lista_cpf_alunos)
        print(user4.codigoturma)
        print(user4.periodo)
        print(user4.turmacodigodisciplina)
        print(user4.turmacpfprofessor)
        print(user4.lista_cpf_alunos)


root = Tk()
Application(root)
root.mainloop()
