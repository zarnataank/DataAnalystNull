
import pandas as pd 
import numpy as np 


data_one=pd.read_csv('googleplaystore.csv')
data_two=pd.read_csv('googleplaystore_user_reviews.csv')


data=pd.merge(data_one,data_two)
data.head(2)

data.shape


data['Installs'].unique()

#. Visualize the sentiment distribution (positive, neutral, negative) of user reviews using a stacked bar chart, segmented by rating groups (e.g., 1-2 stars, 3-4 stars, 4-5 stars). 
# Include only apps with more than 1,000 reviews and group by the top 5 categories.
data['Sentiment'].value_counts()


data['Reviews']=data['Reviews'].astype(int)


data_rev=data.groupby('Reviews').filter(lambda x:len(x)>1000)

top_cat=data['Category'].value_counts().head(5).index


data=data[data['Category'].isin(top_cat)]


data['Rating']=pd.cut(data['Rating'],bins=[2,3,4,5],labels=['1-2 stars','3-4 stars','5 satrs'])


data.groupby('Rating')['Sentiment'].value_counts()


final=data.groupby(['Category','Rating'])['Sentiment'].value_counts().unstack()



import seaborn as sns 
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
final.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Sentiment Distribution by Rating Group and Category')
plt.xlabel('Category')
plt.ylabel('Number of Reviews')
plt.legend(title='Sentiment')
plt.show()
