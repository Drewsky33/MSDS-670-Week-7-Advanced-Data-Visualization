# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:28:08 2021

Andrew Lujan
MSDS 670- Data Visualization
Week 7- Advanced Data Visualization
John Koenig



@author: Andrew
"""

#%%

project_dir = 'C:\\Users\\Andrew\\Desktop\\Data Science Tools\\Regis\\MSDS 670 - Data Visualization\\Week 7'

#%%

# Data source: Kaggle
# https://www.kaggle.com/abcsds/pokemon
# Plotly help: https://plotly.com/python/
# Pokemon dataset tutorials:
   # https://www.kaggle.com/gurarako/plotly-radar-chart-pokemon-part-3
   # https://www.kaggle.com/thebrownviking20/intermediate-visualization-tutorial-using-plotly
# Additional help: https://plotly.com/python/figure-labels/

# Import Libraries
import numpy as np 
import pandas as pd 
#Import plotly libraries
import plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import plotly.graph_objects as go
import plotly
import plotly as py
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
from IPython.display import HTML, Image

init_notebook_mode(connected=True)
plotly.offline.init_notebook_mode(connected=True)





#%%

# Import dataset

df = pd.read_csv('C:\\Users\\Andrew\\Desktop\\Pokemon.csv')

print(df.head())

#%%

# Additional exploration

print(df.describe())


print(df.info())

# The dataset is clean type 2 is null because some Pokemon don't have a second type attribute. 



#%%

trace1 = go.Scatter(
    x = df["Sp. Atk"],
    y = df["Sp. Def"],
    mode='markers',
    marker=dict(
        size= 16,
        color = df["Speed"],#set color equal to a variable
        colorscale='turbo',
        showscale=True
    ),
    text=df["Name"]
)
data = [trace1]
layout = go.Layout(
  paper_bgcolor='rgba(0,0,0,1)',
  plot_bgcolor='rgba(0,0,0,1)',
  showlegend = False,
  font=dict(family='Courier New, monospace', size=10, color='#ffffff'),
  title="Special Defense vs. Special Attack",
  xaxis_title=" Special Attack",
  yaxis_title=" Special Defense",
  
)
fig = go.Figure(data=data, layout=layout)

fig.update_layout(
    title={
        'text': "Sp. Attack vs. Sp. Defense vs. Speed",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

iplot(fig, filename = "Scatterplot")

fig.write_html('Scatterplot.html', auto_open = True)
fig.show(renderer="png")

#%%

psychic = [
    go.Contour(
        x=['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'],
        z=df[df["Type 1"]=="Psychic"].iloc[:,5:11].values,
        colorscale='electric',
    )
]



layout = go.Layout(
    title = "Psychic Pokemon Distribution by Attributes",
    width = 600,
    height = 800,

)




fig = go.Figure(data= psychic, layout=layout)
iplot(fig, filename='Psychic-contour')
fig.write_html('Psychic-contour.html', auto_open = True)
fig.show(renderer="png")


#%%
a = df[df["Name"] == "Blaziken"]
b = df[df["Name"] == "Sceptile"]

data = [
    go.Scatterpolar(
        name = a.Name.values[0],
        r = [a['HP'].values[0],a['Attack'].values[0],a['Defense'].values[0],a['Sp. Atk'].values[0],a['Sp. Def'].values[0],a['Speed'].values[0],a["HP"].values[0]],
        theta = ['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','HP'],
        fill = 'toself',
        line =  dict(
                color = 'red'
            )
        ),
    go.Scatterpolar(
            name = b.Name.values[0],
            r = [b['HP'].values[0],b['Attack'].values[0],b['Defense'].values[0],b['Sp. Atk'].values[0],b['Sp. Def'].values[0],b['Speed'].values[0],b["HP"].values[0]],
            theta = ['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','HP'],
            fill = 'toself',
            line =  dict(
                color = 'green'
            )
        )]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0, 200]
    )
  ),
  showlegend = True,
  title = "{} vs {} Stats Comparison".format(a.Name.values[0], b.Name.values[0])
)

fig = go.Figure(data=data, layout=layout)

fig.layout.images = [dict(
        source="C:\\Users\\Andrew\\Desktop\\pngaaa.com-467203.png",
        xref="paper", yref="paper",
        x=0.05, y=-0.15,
        sizex=0.6, sizey=0.6,
        xanchor="center", yanchor="bottom"
      ),
        dict(
        source="C:\\Users\\Andrew\\Desktop\\pngaaa.com-4083362.png",
        xref="paper", yref="paper",
        x=1, y=-0.15,
        sizex=0.6, sizey=0.6,
        xanchor="center", yanchor="bottom"
      ) ]

fig.write_html('Blaziken_Sceptile_Comparison.html', auto_open = True)

iplot(fig, filename = "Pokemon stats comparison")

fig.show(renderer="png")
