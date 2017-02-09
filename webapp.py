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

@app.route('/')
@app.route("/recipes")
def recipes():
	recipe = session.query(Recipe).all()
	return render_template('recipes.html', recipe = recipe)
@app.route('/')
def order():
	


if __name__ == '__main__':
	app.run(debug=True)