# coding: utf-8
from firebase import firebase

class Usuario:
    firebase = firebase.FirebaseApplication('https://ajudy-2020-tcc.firebaseio.com', None)
    matricula = ""
    nome = ""
    psswd = ""
    curso = ""
    ano = ""
    tipo = ""

    def cadastraUser(self):
        dados = {'nome': self.nome, 'psswd':self.psswd,'curso':self.curso,'ano':self.ano,'tipo':self.tipo}
        result = self.firebase.put('users',self.matricula,dados)
        return result

    def editaUser(self, campo, valor):
        result = self.firebase.put('/users/'+self.matricula, campo, valor)
        return result

    def deletaUser(self):
        result = self.firebase.delete('/users', name=self.matricula)
        return result

    def visualizaUser(self):
        nome = self.firebase.get('/users', name=self.matricula+ '/nome')
        curso = self.firebase.get('/users', name=self.matricula+ '/curso')
        ano = self.firebase.get('/users', name=self.matricula+ '/ano')
        tipo = self.firebase.get('/users', name=self.matricula+ '/tipo')
        values = [self.matricula, nome, curso, ano, tipo]
        return values

    def checkLogin(self):
        checker = False
        psswdCheck = self.firebase.get('/users', name=self.matricula+'/psswd')
        if self.psswd == psswdCheck and self.psswd != None:
            checker = True
        elif psswdCheck == None:
            checker = False
        else:
            checker = False
        return checker

#------ user.* DEVEM SER TROCADOS POR TXT INPUTS/BOXES DO APLICATIVO WEB--------

#TEM Q DESCOMENTAR AS LINHAS CERTAS DE ACORDO COM O TESTE Q TU QUER FAZER

user = Usuario()
user.matricula = '20171inf0222'
user.nome = 'Cleber Jonson'
user.psswd = 'senha1'
user.curso = 'etm'
user.ano = '2'
user.tipo = '1'

user.cadastraUser()
#user.editaUser()
#user.deletaUser()
#valores = user.visualizaUser()
#print("Matricula: ",valores[0])
#print("Nome: ",valores[1])
#print("Curso: ",valores[2])
#print("Ano: ",valores[3])
#print("Tipo: ", valores[4])

#print(user.checkLogin())
