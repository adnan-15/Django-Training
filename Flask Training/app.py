from flask import Flask,request,url_for,redirect,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1>HEllllllo kabutr"

@app.route('/welcome')

def welcome():
    return "<h1>welcome to flask</h1>"

@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/success/<int:a>')

def success(a):
    return "<b>The person is pass and the score is "+str(a)


@app.route('/fail/<int:a>')


def fail(a):
    return "This Student is fail bcoz he/she got "+str(a)


@app.route('/calculate',methods=['POST','GET'])

def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        math=float(request.form['maths'])
        iot=float(request.form['iot'])
        chemistry=float(request.form['chemistry'])
        avg = (math+iot+chemistry)/3
        result=""
        if avg>=80:
            result="success"
        else:
            result="fail"
        return redirect(url_for(result,a=avg))
            
        

if __name__=='__main__':
    app.run(debug=True)