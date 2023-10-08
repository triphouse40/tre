from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import db_cons
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "triphouse"
wara = None


db = sqlite3.connect("frr.db")

# File names for different stylesheets/fonts and more
finame = "static/fkfk.css"
foname = ["Default", "Patrick Hand", "Great Vibes", "Permanent Marker", "Sedgwick Ave Display", "Indie Flower"]


@app.route("/", methods=["POST", "GET"])
def index():
	if not (session):
		return redirect("/login")
	
	# fetching the persons known ppl
	gwem = session["user"]
	peron = list(db_cons.thread_func(f"SELECT id FROM users WHERE username = '{gwem}'"))[0][0]
	quu = list(db_cons.thread_func(f"SELECT un_known.knowns FROM un_known JOIN users ON un_known.person_id = users.id WHERE users.username = '{gwem}';"))
	umber_list = []
	if quu:
		for personss in quu[0]:
			umber_list = [int(num_str) for num_str in personss.split()]
	
	knoww = []
	for personn in umber_list:
		# fetching the usernames
		qur = db_cons.thread_func(f"SELECT username FROM users WHERE id = '{personn}';")
		if qur:
			personn = list(qur)[0][0]
			knoww.append(personn)

	no_knoww = []
	que = list(db_cons.thread_func("SELECT username FROM users;"))
	for perso in que:
		if perso[0] not in knoww and perso[0] != session["user"]:
			no_knoww.append(perso[0])

	# To read messages
	megases = list(db_cons.thread_func("SELECT receivers FROM messges;"))
	recheiver = {}
	iko = []
	for x in megases:
		iko = [int(ee) for ee in x[0].split()]
		recheiver = set(iko)

	for ys in iko:
		if ys in recheiver:
			ys = str(ys)
			mssage = list(db_cons.thread_func(f"SELECT message FROM messges WHERE receivers LIKE '%{ys}%' ;"))
			if peron == int(ys) and int(ys) == peron:
				megases = mssage
				print("okkkk")
				break
			else:
				print("yyy")
				megases = None
	

	# For sending messages
	if request.method == "POST":
		# Getting the type of buttons posted
		ee = request.form
		peeps = ee.get("peeps")
		messagge = ee.get("veng")
		if peeps:
			db_cons.thread_func(f"INSERT INTO messges (person_id, receivers, message) VALUES ('{peron}', '', '{messagge}');")
			peeps = [u for u in peeps.split()]
			for i in peeps:
				perp_id = list(db_cons.thread_func(f"SELECT id FROM users WHERE username = '{i}'"))[0][0]
				datte = list(db_cons.thread_func(f"SELECT date, receivers FROM messges WHERE person_id = '{peron}' ORDER BY date DESC LIMIT 1;"))[0]
				db_cons.thread_func(f"UPDATE messges SET receivers = '{perp_id} {datte[1]}' WHERE person_id = '{peron}' AND date = '{datte[0]}'")
			
	if request.method == "GET":
		pass

	return render_template("index.html", userr=session["user"], fontss=foname, knoww=knoww, no_knoww=no_knoww, messsgas=megases)

@app.route("/login", methods=["POST", "GET"])
def login():
	
	if request.method == "POST":
		user = request.form["userr"]
		pword = request.form['pword']
		wara = f"SELECT username, pwww FROM users WHERE username = '{user}';"
		jeng = list(db_cons.thread_func(wara))

		if not jeng:
			return redirect("/login")
		
		if pword is None:
			return redirect("/login")

		elif check_password_hash(jeng[0][1], pword):
			session["user"] = user
			return redirect("/")
		


	return render_template("login.html", loggi=finame)

@app.route("/registar", methods=["POST", "GET"])
def registar():
	if request.method == "POST":
		user = request.form.get("userr")
		pword = request.form.get("pwerd")
		pword = generate_password_hash(pword)


		qur1 = f"SELECT username from users WHERE username = '{user}';"
		perss = list(db_cons.thread_func(qur1))
		
		if len(perss) != 0:
			print("GGG ", perss)
			return redirect("/registar")
		

		db_cons.thread_func(f"INSERT INTO users (username, pwww) VALUES ('{user}', '{pword}')")
		# 					f"INSERT INTO un_known (knowns) SELECT 'chicken' FROM users WHERE users.id = '{user}'")
		
		que1 = f"SELECT username, id from users WHERE username = '{user}';"
		pers1 = list(db_cons.thread_func(que1))
		db_cons.thread_func(f"INSERT INTO un_known (knowns, person_id) SELECT '', users.id FROM users WHERE users.id = '{pers1[0][1]}'")

		session["user"] = user
		
		return redirect("/")
	
	
	return render_template("registar.html")

# logging out
@app.route("/logout", methods=["POST", "GET"])
def logout():
	if request.method == "POST":
		print("Ayoo wazzup")
		session.pop("user", None)
		return redirect("/login")

if __name__ == '__main__':
	app.run(debug=True)