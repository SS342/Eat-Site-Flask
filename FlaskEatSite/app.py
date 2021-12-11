import flask
from flask import Flask, render_template
from flask import request as flask_request
from flask_sqlalchemy import SQLAlchemy

MainApp = Flask(__name__)
MainApp.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///allelleo.db'
MainApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(MainApp)

@MainApp.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    MainApp.run(debug=True)