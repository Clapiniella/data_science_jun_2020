import os, sys
import pandas as pd
from IPython.display import Image
import seaborn as sns
import matplotlib.pyplot  as plt
import xlrd
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.io as pio
from bubbly.bubbly import bubbleplot
import random
import plotly


os.path.abspath('')
root_path = os.path.dirname(os.path.abspath(''))
sys.path.append(root_path)

def treemap_show(df):
    print("Done")
    fig = px.treemap(df, path=[df.index], 
                values='Score',title="Country names based on Happiness score")
    fig.show()
    

def test():
    print("I'm working")

def top5_show(df, year):
    fig = px.bar(data_frame = df.nlargest(5,"Score"),
             y=df.nlargest(5,"Score").index,
             x="Score",
             orientation='h',
             color=df.nlargest(5,"Score").index,
             text="Score",
             color_discrete_sequence=px.colors.qualitative.D3)
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

    fig.update_traces(texttemplate='%{text:.4s}', 
                  textposition='inside', 
                  marker_line_color='rgb(255,255,255)', 
                  marker_line_width=2.5, 
                  opacity=0.7)
    fig.update_layout(width=600,
                  showlegend=False,
                  title="Top 5 happiest countries in {}".format(year))
    fig.show()
    #plotly.offline.plot(fig, filename='top_5.html')

def lowest10_show(df):
    fig1 = px.bar(data_frame = df.nsmallest(10,"Score"),
             y=df.nsmallest(10,"Score").index,
             x="Score",
             orientation='h',
             color=df.nsmallest(10,"Score").index,
             text="Score",
             color_discrete_sequence=px.colors.qualitative.D3)
    fig1.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

    fig1.update_traces(texttemplate='%{text:0.2f}',
                  textposition='inside', 
                  marker_line_color='rgb(255,255,255)', 
                  marker_line_width=2.5, 
                  opacity=0.7)
    fig1.update_layout(width=800,
                  showlegend=False,
                  title="Top 10 unhappiest countries",)
    fig1.show()

def score_order_bar(df, year):
    fig = px.bar(df, x=df.index, y='Score',color='Score',height=600)
    fig.update_layout(title='Countries in order of Happiness Score in {}'.format(year),titlefont_size=20)
    fig.show()
    #plotly.offline.plot(fig, filename='Score_order_bar.html')


def scatter_show(df, column, size):
    fig = px.scatter(df, x=column, y="Score",
	         size=size, color=df.index,height=750,
                 hover_name=df.index, log_x=True, size_max=60)
    fig.update_layout(title="Happiness Score vs {}, bubble size based on {}".format(column, size))
    fig.show()
    #plotly.offline.plot(fig, filename='Scatter.html')

def distribution_show(df, year):
    fig = px.histogram(df["Score"],
                   marginal="box")
    fig.update_traces(opacity=0.7,
                      marker_line_color='rgb(255,255,255)', 
                      marker_line_width=2.5
                      )
    fig.update_layout(showlegend=False,
                  title="Distribution of the happiness score in {}".format(year),
                  width=600)
    fig.show()
    #plotly.offline.plot(fig, filename='distribution.html')

def tendency(df, column):
    fig=px.line(df,x='Year',y=column, color=df.index,template="plotly_dark")
    fig.update_layout(title="Trend of {}".format(column))
    fig.show()
    #plotly.offline.plot(fig, filename='tendency.html')


def df_to_corr(df, year):
    df_corr = df.drop(axis=1, columns="Year")
    plt.figure(figsize=(10,8))
    sns.heatmap(df_corr.corr(), annot=True, fmt='.2g', center= 0, cmap= 'coolwarm', linewidths=2, linecolor='black')
    plt.title("Correlation Happiness dataset {}".format(year))
    plt.show()

def globe_happiness_score(df):
    trace1 = [go.Choropleth(
               colorscale = 'Picnic',
               locationmode = 'country names',
               locations = df.index,
               text = df.index, 
               z = df["Score"],
               colorbar=dict(title="Score")
               )]

    layout = dict(title = 'Average Happiness Score 2015-2019',
                  geo = dict(
                      showframe = True,
                      showocean = True,
                      showlakes = True,
                      showcoastlines = True,
                      projection = dict(
                          type = 'hammer'
             )))


    annot = list([ dict( x=0.1, y=0.8, text='Projection', yanchor='bottom', 
                    xref='paper', xanchor='right', showarrow=False )])

    
    layout[ 'annotations' ] = annot


    fig = go.Figure(data = trace1, layout = layout)
    py.iplot(fig)
    #plotly.offline.plot(fig, filename='World_happiness_globe.html')

def pie(df):
    pie = px.pie(
        data_frame=df,
        values= "time_in_hours",
        names=df.index,
        color=df.index,
        hover_name="time_in_hours",
        labels={"time_in_hours":"Number of hours worked:", "index":"Step:"},
        title="Distribution of time per step in the project",
        template="presentation",
        width=800,
        height=600,
        hole=0.3)

    pie.update_traces( marker=dict(line=dict(color="#000000", width=0.5)))
    pie.show()
    #plotly.offline.plot(fig, filename='time_pie.html')
    
