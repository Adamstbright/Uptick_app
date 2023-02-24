from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy   #We have downloaded psycopg2 for postgresql and we are using sqlalchemy to create the table.

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='postgresql://adamstbright:tobebe1995@localhost/height'      #This is connection of the database to the app and you must include the database name, username and passsword in tne url. app here is the app document we are creating.
db=SQLAlchemy(app)          #connecting to the database

class Data(db.model):
    __tablename__="data"    #This is use to create the table in the database. this class entirely is use for the table creation in the database.
    id=db.Column(db.Integer, primary_key=True)    #THis is to create id column in the table
    email_=db.Column(db.string(120), unique=True)  #This is to create email column in the table
    height_=bd.Column(db.Integer)              #THis is to create height_ column in the table (_ after the height is to distinguish it from height variable that we have in successfuntion)

    def __init__(self, email_, height_):    # This function is to initialise the variables of the objects.
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods={'POST'})
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email,height)
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
