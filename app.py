from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder='templates')


# Load your trained model
model = joblib.load('model.pkl')  # Make sure to replace with the correct path

@app.route('/')
def index():
    return render_template('index.html')  # This is the page with the form

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extracting form data from the request
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])
        
        # Prepare the feature vector (you may need to preprocess this based on your model)
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Make prediction using the loaded model
        prediction = model.predict(features)
        
        # Render result on result.html, pass the prediction
        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
