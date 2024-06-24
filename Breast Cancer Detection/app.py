
import flask
from flask import Flask , request , render_template

import pandas
import pickle
import numpy

model = pickle.load(open("model.pkl",'rb'))

app= flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route("/predict",methods=['POST'])

def predic():
  pass

if __name__== "__main__":
  app.run(debug=True)


