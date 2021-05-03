#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/lr_model.pkl', 'rb') as f:
    logistic = pickle.load(f)



def get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal, req_model):
    mylist = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':

        import pdb
        pdb.set_trace()

        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        rbp = request.form['rbp']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        max = request.form['max']
        exang = request.form['exang']
        old = request.form['old']
        slope = request.form['slope']
        nvessels = request.form['nvessels']
        thal = request.form['thal']

        req_model = 'Logistic'

        target = get_predictions(age, sex, cp, rbp, chol, fbs, restecg, max,
        exang, old, slope, nvessels, thal, req_model)

        if target==1:
            heart_defect = 'Patient is likely to have heart defect'
        else:
            heart_defect = 'Patient is unlikely to buy heart defect'

        return render_template('home.html', target = target, heart_defect = heart_defect)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)