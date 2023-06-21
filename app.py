from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/bmi', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = round(num2/(num1/100)**2,2)

    birthday = request.form['birthday']
    today = date.today()
    birth_date = date.fromisoformat(birthday)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座",
                        "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蝎座", "射手座", "魔羯座")

    return render_template('bmi.html', result=result,dates=dates,constellations=constellations,age=age,birth_date=birth_date)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')