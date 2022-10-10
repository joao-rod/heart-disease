from sklearn.tree import ExtraTreeClassifier
from flask import Flask, render_template, request

import pickle
model = pickle.load(open('../../models/modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('components.html')

@app.route('/result', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        imc = float(weight / (height * height))
        
        smoking = float(request.form.get('smoking'))
        drink = float(request.form.get('drink'))
        stroke = float(request.form.get('stroke'))
        physical = float(request.form.get('physical'))
        mental = float(request.form.get('mental'))
        diff = float(request.form.get('diff'))
        sex = float(request.form.get('sex'))
        age = float(request.form.get('age'))
        race = float(request.form.get('race'))
        diabetic = float(request.form.get('diabetic'))
        activity = float(request.form.get('activity'))
        generalHealt = float(request.form.get('generalHealt'))
        sleep = float(request.form.get('sleep'))
        asthma = float(request.form.get('asthma'))
        kidney = float(request.form.get('kidney'))
        cancer = float(request.form.get('cancer'))
        
        predict = model.predict([[
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
        
        if predict[0] == 1:
            result = "não possui"
        else:
            result = "possui"

    return render_template('result.html', result=result)

app.run(debug=True, host='0.0.0.0')