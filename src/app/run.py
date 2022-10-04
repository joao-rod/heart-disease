from sklearn.tree import ExtraTreeClassifier
from flask import Flask, render_template, request

import pickle
model = pickle.load(open('modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('components.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        imc = request.form.get('imc')
        smoking = request.form.get('smoking')
        drink = request.form.get('drink')
        stroke = request.form.get('stroke')
        physical = request.form.get('physical')
        mental = request.form.get('mental')
        diff = request.form.get('diff')
        sex = request.form.get('sex')
        age = request.form.get('age')
        race = request.form.get('race')
        diabetic = request.form.get('diabetic')
        activity = request.form.get('activity')
        generalHealt = request.form.get('generalHealt')
        sleep = request.form.get('sleep')
        asthma = request.form.get('asthma')
        kidney = request.form.get('kidney')
        cancer = request.form.get('cancer')
        result = model.predict([[
            imc,
            smoking,
            drink,
            stroke,
            physical,
            mental,
            diff,
            sex,
            age,
            race,
            diabetic,
            activity,
            generalHealt,
            sleep,
            asthma,
            kidney,
            cancer
        ]])
        print(result)
    return "<script>alert('teste)</script>"

app.run(debug=True)