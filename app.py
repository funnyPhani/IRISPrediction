import numpy as np
import pandas as pd
import seaborn as sns
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

dataset = sns.load_dataset('iris')

dataset_X = dataset.iloc[:,[0,1,2,3]].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
dataset_scaled = sc.fit_transform(dataset_X)
dataset_scaled = sc.fit_transform(dataset_X)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict( sc.transform(final_features) )

    if prediction == 0:
        pred = "setosa"
    elif prediction == 1:
        pred = "virginica"
    else:
        pred='versicolor'
        
    output = pred

    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
