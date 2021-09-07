from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/animus_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
# app.config.from_object(DevConfig)

db=SQLAlchemy(app)
# api=Api(app, doc='/docs') 

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(30))

    def __init__(self, username, password):
        self.username=username
        self.password=password


@app.route("/")
def login():
    return render_template('index.html',token='Hello react')

if __name__=='__main__':
    app.run(debug=True)