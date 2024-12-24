import pandas as pd 
import numpy as np 
app_store_reviews = pd.read_csv("labeled_app_store_reviews.csv", sep=';')
app_store_reviews.head(2)
app_store_reviews.info()
app_store_reviews['country'].unique()
data={'app':['Home Workout - No Equipment',
       '30 Day Fitness Challenge - Workout at Home',
       'Home Workout for Men - Bodybuilding',
       'Fat Burning Workout - Home Weight lose', 'Fitbit',
       'Cycling - Bike Tracker', 'Abs Training-Burn belly fat',
       'Calorie Counter - EasyFit free', 'Garmin Connect™',
       'BetterMe: Weight Loss Workouts',
       'Ever After High™ Charmed Style', 'CVS Caremark',
       'Castlight Mobile', 'Anthem BC Anywhere', 'ConnectLine',
       'HTC Social Plugin - Facebook', 'Chilindo', 'Camera FV-5',
       'Color Touch Effects', 'Foursquare Swarm: Check In',

       ],
       'Category':['HEALTH_AND_FITNESS', 'GAME', 'FAMILY', 'SPORTS', 'PRODUCTIVITY','HEALTH_AND_FITNESS', 
       'HEALTH_AND_FITNESS', 'GAME', 'FAMILY','SPorts', 'HEALTH_AND_FITNESS', 
       'HEALTH_AND_FITNESS', 'GAME', 'FAMILY','SPorts',  'HEALTH_AND_FITNESS', 
       'HEALTH_AND_FITNESS', 'GAME', 'FAMILY','SPorts', 
       
       ],
       'Installs':['10,000,000+', '1,000,000+', '100,000+', '500,000+', '5,000,000+',
       '50,000,000+', '500,000,000+', '100,000,000+', '50,000+','50,000,000+',
        '500,000,000+', '100,000,000+', '50,000+','50,000+',
       '10,000+','10,000,000+', '1,000,000+', '100,000+', '500,000+', '5,000,000+',],

       'Country':['Australia', 'India', 'UK', 'Brazil', 'USA',
       'Australia', 'India', 'UK', 'Brazil', 'USA',
       'Australia', 'India', 'UK', 'Brazil', 'USA','Australia', 'India', 'UK', 'Brazil', 'USA',
      
       ]
       
    }
    df = pd.DataFrame(data)
    df.head(2)
    df['Installs']=df['Installs'].str.replace('+', '')
df['Installs'] = df['Installs'].str.replace(',', '')
df.head(2)
df['Installs']=df['Installs'].astype(int)
df_filtered = df[~df['Category'].str.startswith(('A', 'C', 'G', 'S'))]
df_filtered = df_filtered[df_filtered['Installs'] > 1000000]
df_filtered = df_filtered.nlargest(5, 'Installs')
df_filtered.head(2)
df_filtered.shape
import datetime
import pytz
import plotly.graph_objects as go

fig = go.Figure(data=go.Choropleth(
    locations=['World'] * len(df_filtered), 
    z=df_filtered['Installs'].astype(float),
    text=df_filtered['Category'],
    colorscale='Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title='Number of Installs'
))

# Update layout
fig.update_layout(
    title_text='Global Installs by Category',
    geo=dict(
        showland=True,
        showcoastlines=True,
        showframe=False,
        countrycolor='lightgray',
        projection_type='equirectangular'
    ),
)
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
if 18 <= current_time.hour <= 22: # 6 PM IST to 10 PM IST
    fig.show()
else:
    print("Graph is not available at this time.")
