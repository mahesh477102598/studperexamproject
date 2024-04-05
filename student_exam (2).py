

# Students Performance in Exams

# importing libraries and dataset
"""

import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
# Plotly Libraris
import plotly.express as px
import plotly.graph_objects as go


import warnings
warnings.filterwarnings("ignore")
student=pd.read_csv("StudentsPerformance123.csv")
df=student.copy()
df.head()

"""# bar plot seaborn

"""

ax = sns.barplot(x="race", y="math score", data=df)
plt.ylabel('Math Score')
plt.xlabel('Race')
plt.title('Math Score With Race');

"""# scatter plot seaorn"""

sns.scatterplot(data=df, x="math score", y="reading score")
plt.ylabel('Reading Score')
plt.xlabel('Math Score')
plt.title('Reading Score With Math Score');

"""#  Line Plot Seaborn"""

sns.lineplot(data=df, x="math score", y="reading score",hue='gender')
plt.ylabel('Reading Score')
plt.xlabel('Math Score')
plt.title('Reading Score Vs Math Score With Gender');

"""# pie plot seaborn

"""

# Race rates according in data

labels = df.race.value_counts().index
colors = ['grey','blue','red','yellow','green']
explode = [0.1,0,0,0,0]
sizes = df.race.value_counts().values

# visual
plt.figure(figsize = (7,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Race ',color = 'blue',fontsize = 15);

"""# pairplot plot"""

sns.pairplot(df, hue="gender");

"""# Sunburst Plot Plotly"""

fig = px.sunburst(df, path=['gender', 'race','parental level of education',], values='math score',
                   color=df['math score'],
                  color_continuous_scale='electric')
fig.show()

"""# Point Plot"""

ax = sns.pointplot(y="math score", x="gender", data=df,hue='lunch',palette="gnuplot")
plt.xlabel('Gender')
plt.ylabel('Math Score');