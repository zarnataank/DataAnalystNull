import pandas as pd 
import numpy as np 
data_one=pd.read_csv('googleplaystore.csv')
data_two=pd.read_csv('googleplaystore_user_reviews.csv')
data=pd.merge(data_one,data_two)
data.head(2)
data['App'].unique()
cat_Counts=data['Category'].value_counts()
top_cat=cat_Counts[cat_Counts>50].index
data=data[data['Category'].isin(top_cat)]
data=data[data['App'].str.contains('C')]
data['Reviews']=data['Reviews'].astype(int)
data['Rating']=data['Rating'].astype(int)
data=data[data['Reviews']>=10]
data=data[data['Rating']<4.0]
new_df=data.copy()
categories=data['Category'].unique()

import plotly.graph_objects as go
from datetime import datetime
import pytz

fig = go.Figure(data=go.Violin(
    x=new_df['Category'],
    y=new_df['Rating'],
    box_visible=True,
    meanline_visible=True,
    fillcolor='blue',
    opacity=0.5
))
fig.show()
import plotly.graph_objects as go
from datetime import datetime
import pytz

fig_sec = go.Figure(data=go.Violin(
    x=new_df['App'],
    y=new_df['Rating'],
    box_visible=True,
    meanline_visible=True,
    fillcolor='blue',
    opacity=0.5
))
ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))
if 16 <= ist_time.hour < 18:
    for category in categories:
        category_df = new_df[new_df['Category']== category]
        ratings = category_df['Rating']
       
        # Add the violin plot for the current category to the figure
        fig.add_trace(go.Violin(
            x=ratings,
            box_visible=True,
            meanline_visible=True,
            fillcolor='blue',
            opacity=0.5,
            name=category
        ))
        fig.update_layout(
        title_text='Distribution of Ratings by Category',
        xaxis_title='Category',
        yaxis_title='Rating'
    )
    fig.show()