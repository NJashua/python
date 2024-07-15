import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv(r"MachineLearning\train.csv")
print(data['Credit_Score'].value_counts())
fig = px.box(data, 
             x="Credit_Score",  
             y = "Payment_of_Min_Amount",
             color="Credit_Score", 
             title="Credit Scores Based on Occupation", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod= "exclusive")
fig.show()