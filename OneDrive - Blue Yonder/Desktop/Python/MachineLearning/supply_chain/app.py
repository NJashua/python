from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

def load_data():
    data = pd.read_csv(r'MachineLearning\train.csv')
    return data

def create_visualizations(data):
    fig_credit_score = px.histogram(data, x='Credit_Score', title='Credit Score Distribution')
    graphJSON_credit_score = json.dumps(fig_credit_score, cls=PlotlyJSONEncoder)

    fig_income_vs_salary = px.scatter(data, x='Annual_Income', y='Monthly_Inhand_Salary', title='Annual Income vs Monthly Inhand Salary')
    graphJSON_income_vs_salary = json.dumps(fig_income_vs_salary, cls=PlotlyJSONEncoder)

    fig_age = px.histogram(data, x='Age', title='Age Distribution')
    graphJSON_age = json.dumps(fig_age, cls=PlotlyJSONEncoder)

    fig_graph = px.box(data, x='Credit_Score', y='Payment_of_Min_Amount', color='Credit_Score', 
                       title='Credit Scores Based on Occupation', 
                       color_discrete_map={'Poor': 'red', 'Good': 'green', 'Standard': 'yellow'})
    fig_graph.update_traces(quartilemethod='exclusive')
    graphJSON_fig_graph = json.dumps(fig_graph, cls=PlotlyJSONEncoder)

    return graphJSON_credit_score, graphJSON_income_vs_salary, graphJSON_age, graphJSON_fig_graph

@app.route('/')
def index():
    data = load_data()
    graphJSON_credit_score, graphJSON_income_vs_salary, graphJSON_age, graphJSON_fig_graph = create_visualizations(data)
    return render_template('index.html', 
                           graphJSON_credit_score=graphJSON_credit_score,
                           graphJSON_income_vs_salary=graphJSON_income_vs_salary,
                           graphJSON_age=graphJSON_age,
                           graphJSON_fig_graph=graphJSON_fig_graph)

if __name__ == '__main__':
    app.run(debug=True)
