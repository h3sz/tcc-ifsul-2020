# coding: utf-8
from firebase import firebase

class Grupo:
    firebase = firebase.FirebaseApplication('https://ajudy-2020-tcc.firebaseio.com', None)
    criador = ""
    materia = ""
    descr = ""
    ano = ""
    semestre = ""
    data = ""
    hora = ""
    local = ""
    tamanho = ""

    def criaGrupo(self):
        idGrupo = (self.criador+"|"+self.materia+"|"+self.ano+"|"+self.semestre)
        dados = {'criador': self.criador, 'materia':self.materia,'descr':self.descr,'ano':self.ano,'semestre':self.semestre,'semestre':self.semestre,'data':self.data,'hora':self.hora,'local':self.local,'tamanho':self.tamanho}
        print (idGrupo)
        self.firebase.put('grupos',idGrupo,dados)
        path = ('/grupos/' + idGrupo + '/participantes')
        self.firebase.put(path, self.criador, self.criador)

    def deletaGrupo(self, idGrupo):
        #idGrupo = (self.criador + "|" + self.materia + "|" + self.ano + "|" + self.semestre)
        self.firebase.delete('/grupos', name=idGrupo)

    def entraGrupo(self, matr, idGrupo):
        #idGrupo = (self.criador + "|" + self.materia + "|" + self.ano + "|" + self.semestre)
        path = ('/grupos/' + idGrupo + '/participantes')
        self.firebase.put(path, matr, matr)

    def saiGrupo(self, matr, idGrupo):
        #idGrupo = (self.criador + "|" + self.materia + "|" + self.ano + "|" + self.semestre)
        path = ('/grupos/' + idGrupo + '/participantes')
        self.firebase.delete(path, name=matr)

    def getGrupos(self):
        values = self.firebase.get('/grupos', None)
        grupos = []
        gruposFinal = []
        for k in values.keys():
            grupos.append(values[k])
        for x in range (len(grupos)):
            line = []
            line.append(grupos[x]['criador'])
            line.append(grupos[x]['materia'])
            line.append(grupos[x]['ano'])
            line.append(grupos[x]['semestre'])
            line.append(grupos[x]['data'])
            line.append(grupos[x]['hora'])
            line.append(grupos[x]['local'])
            line.append(grupos[x]['participantes'])
            line.append(grupos[x]['tamanho'])
            line.append(grupos[x]['descr'])
            gruposFinal.append(line)

        return gruposFinal

    def getGruposCriador(self, matr):
        values = self.firebase.get('/grupos', None)
        grupos = []
        gruposFinal = []
        for k in values.keys():
            grupos.append(values[k])
        for x in range (len(grupos)):
            if grupos[x]['criador'] == matr:
                line = []
                line.append(grupos[x]['criador'])
                line.append(grupos[x]['materia'])
                line.append(grupos[x]['ano'])
                line.append(grupos[x]['semestre'])
                line.append(grupos[x]['data'])
                line.append(grupos[x]['hora'])
                line.append(grupos[x]['local'])
                line.append(grupos[x]['participantes'])
                line.append(grupos[x]['tamanho'])
                line.append(grupos[x]['descr'])
                gruposFinal.append(line)
        return gruposFinal

#------------- area de testes

#grupo = Grupo()

#grupo.criador = '20171inf0279'
#grupo.materia = 'matematica'
#grupo.descr = 'grupo para estudar portugues'
#grupo.ano = '4'
#grupo.semestre = '2'
#grupo.data = '18/03/2020'
#grupo.hora = '11:48'
#grupo.local = 'apoio'
#grupo.tamanho = '4'
#grupo.participantes = ''

#grupo.criaGrupo()
#grupo.entraGrupo('20171inf180')
#grupo.saiGrupo('20171inf180')
#grupo.deletaGrupo()
#grupo.getGrupos()


