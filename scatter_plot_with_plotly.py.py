# -*- coding: utf-8 -*-
"""scatter_plot_with_plotly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c6Yt4ouOWlyHTahUoKDm-Ntb5pjL5I6g
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import iplot
import plotly.graph_objs as go

from google.colab import drive
drive.mount('/content/drive')

timesData = pd.read_csv("/content/drive/MyDrive/timesData.csv")

timesData.head()

df2014 = timesData[timesData.year == 2014].iloc[:100,:]
df2015 = timesData[timesData.year == 2015].iloc[:100,:]
df2016 = timesData[timesData.year == 2016].iloc[:100,:]

trace1 = go.Scatter(
      x = df2014.world_rank,
      y = df2014.citations,
      mode = "markers",
      name = "2014",
      marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
      text= df2014.university_name)

trace2 = go.Scatter(
      x = df2015.world_rank,
      y = df2015.citations,
      mode = "markers",
      name = "2015",
      marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
      text= df2015.university_name)

trace3 = go.Scatter(
      x = df2016.world_rank,
      y = df2016.citations,
      mode = "markers",
      name = "2016",
      marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
      text= df2016.university_name)

data = [trace1, trace2, trace3]

layout = dict(title = 'Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False))

fig = dict(data = data, layout = layout)

iplot(fig)

trace1 =go.Scatter( 
                    x = df2014.world_rank,
                    y = df2014.total_score,  
                    mode = "markers",      
                    name = "2014",         
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'), 
                    text= df2014.university_name)  

trace2 =go.Scatter(
                    x = df2015.world_rank, 
                    y = df2015.total_score,  
                    mode = "markers",      
                    name = "2015",         
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),  
                    text= df2015.university_name)  

trace3 =go.Scatter(
                    x = df2016.world_rank, 
                    y = df2016.total_score,  
                    mode = "markers",      
                    name = "2016",        
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),  
                    text= df2016.university_name)  

data = [trace1, trace2, trace3]  

layout = dict(title = 'Total score vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Total Score',ticklen= 5,zeroline= False) 
             )
fig = dict(data = data, layout = layout)  

iplot(fig)