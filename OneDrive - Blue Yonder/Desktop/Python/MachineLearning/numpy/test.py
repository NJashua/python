# import numpy as np

# arr = np.array(list("hey nithin"))
# res = np.array_split(arr, 2)
# print(res)

from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

def load_data():
    data = pd.read_csv(r"MachineLearning\train.csv")
    return data

def get_graph(data):
    fig = px.line(data, x='Name', y="Num_of_Delayed_Payment")
    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON

@app.route("/")
def index():
    data = load_data()
    graphJSON = get_graph(data)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)