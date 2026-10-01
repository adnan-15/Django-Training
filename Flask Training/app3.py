from flask import redirect,url_for,render_template,request,Flask
from flask_sqlalchemy import SQLAlchemy

app3 = Flask(__name__)

#database configuration code 
app3.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskproject'
app3.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Adnan")
db = SQLAlchemy(app3)

class Employee(db.Model):
    Eno=db.Column(db.Integer,primary_key=True)
    Ename=db.Column(db.String(20),nullable=True)
    Eemail=db.Column(db.String(20),nullable=True)
    Ephone_num=db.Column(db.String(12),nullable=True)
    Ecompany=db.Column(db.String(80),nullable=True)
with app3.app_context():
    db.create_all()

if __name__=="__main__":
    app3.run(debug=True)