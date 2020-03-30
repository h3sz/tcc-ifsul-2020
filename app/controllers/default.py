from flask import *
from app import app
import usuario
import grupo

session = '20171inf0666'

@app.route("/index")
@app.route('/', methods=['GET', 'POST'])
def index():
	err = "Matricula e/ou senha errado(s)"
	if request.method == 'POST':
		if request.form['submit'] == 'submit':
			user = usuario.Usuario()
			user.matricula = request.form['matricula']
			user.psswd = request.form['senha']
			check = user.checkLogin()
			group = grupo.Grupo()
			listGrupos = ['teste','teste','teste']
			listGrupos = group.getGrupos()
			if check == True:
				return redirect(url_for('frontPage'))
			if check == False:
				return render_template("index.html")
	return render_template("index.html")

@app.route("/frontPage", methods=['GET', 'POST'])
def frontPage():
	group = grupo.Grupo()
	listGrupos = []
	listGrupos = group.getGrupos()
	if request.method == 'POST':
		if request.form['submit'] == 'entrar':
			group = grupo.Grupo()
			idGrupo = request.form['id']
			group.entraGrupo(session, idGrupo)
			return redirect(url_for('frontPage'))	
		elif request.form['submit'] == 'sair':
			group = grupo.Grupo()
			idGrupo = request.form['id']
			group.saiGrupo(session, idGrupo)
			return redirect(url_for('frontPage'))	
	return render_template("frontPage.html", listGrupos = listGrupos)

@app.route("/createGroupPage", methods=['GET', 'POST'])
def createGroupPage():
	if request.method == 'POST':
		if request.form['submit'] == 'salvar':
			group = grupo.Grupo()
			group.criador = session
			group.materia = request.form['materiaGrupo']
			group.ano = request.form['anoGrupo']
			group.semestre = request.form['semestreGrupo']
			group.local = request.form['localGrupo']
			group.tamanho = request.form['tamanhoGrupo']
			group.descr = request.form['bioGrupo']
			group.data = request.form['dataGrupo']
			group.hora = request.form['horaGrupo']
			group.criaGrupo()
			return redirect(url_for('myGroupPage'))
	return render_template("createGroupPage.html")

@app.route("/myGroupPage", methods=['GET', 'POST'])
def myGroupPage():
	if request.method == 'POST':
		if request.form['submit'] == 'delete':
			group = grupo.Grupo()
			idGrupo = request.form['id']
			group.deletaGrupo(idGrupo)
			return redirect(url_for('myGroupPage'))	
	group = grupo.Grupo()
	criadoGrupos = []
	criadoGrupos = group.getGruposCriador(session)
	return render_template("myGroupPage.html", criadoGrupos = criadoGrupos)

@app.route("/profilePage")
def profilePage():
	return render_template("profilePage.html")

@app.route("/treePage")
def treePage():
	return render_template("treePage.html")

@app.route("/createAccount")
def createAccount():
	return render_template("createAccount.html")