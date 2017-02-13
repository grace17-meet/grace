from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
#from flask import session as login_session
#from model import *
from werkzeug.utils import secure_filename
import locale, os
# from werkzeug.contrib.fixers import ProxyFix
# from flask_dance.contrib.github import make_github_blueprint, github

#UPLOAD_FOLDER = 'uploads'
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.wsgi_app = ProxyFix(app.wsgi_app)
# blueprint = make_github_blueprint(
#     client_id="TODO",
#     client_secret="TODO",
# )
# app.register_blueprint(blueprint, url_prefix="/login")

#engine = create_engine('sqlite:///fizzBuzz.db')
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine, autoflush=False)
#session = DBSession()


@app.route('/')
def showMainPage():
	return render_template('homepage.html')
@app.route('/newTaster', methods = ['GET', 'POST'])
def newTaster():
	if request.method == 'POST':
		name= request.form['name']
		email = request.form['email']
		password = request.form['password']
		address = request.form['address']
		if name =="" or email == "" or password == "":
			flash ("Your missing some arguments")
			return redirect(url_for('newTaster'))
		if session.query(Customer).filter_by(email = email).first() is not None:
			flash("A user with this email already exists")
			return redirect(url_for('newTaster'))
		taster = Taster(name = name, email = email, address = address )
		taster.hash_password(password)
		session.add(taster)
		session.commit()
		flash("Welcome!")
	else:
		return render_template('newTaster.html')
		flash("Please try again")

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")   
    elif request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        if email is None or password is None:
            flash("Missing some Arguments")
            return redirect(url_for("login"))
        if verify_password(email,password):
            customer = session.query(Member).filter_by(email = email).one()
            flash("Login Succesful,start tasting! %s" % member.name)
            login_session['name'] = member.name
            login_session['email'] = member.email
            login_session['id'] = member.id
            return redirect(url_for("inventory"))
        else:
            flash('Incorrect username/password ')
            return redirect(url_for("login"))
            
@app.route('/logout', methods = ['POST'])
def logout():
	return "To be implmented"



@app.route("/recipes")
def recipes():
	recipe = session.query(Recipe).all()
	return render_template('recipes.html', recipe = recipe)

@app.route("/history")

def history():
	history = session.query(History).all()
	return render_template('history.html', history = history)

@app.route("/aboutme")
def aboutme():
	aboutme = session.query(Aboutme).all()
	return render_template('aboutme.html', aboutme= aboutme)
@app.route("/addrecipe")
def addrecipe():
	addrecipe = session.query(Addrecipe).all()
	return render_template('addrecipe.html', addrecipe = addrecipe)

if __name__ == '__main__':
   app.run(debug=True)