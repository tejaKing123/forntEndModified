import numpy as np
import os
import pandas as pd
from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    op = "fuckshit"
    return render_template('floods.html', text='{}'.format(op))


if __name__ == "__main__":
    app.run(debug=True)
