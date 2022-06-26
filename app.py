#Pie Chart
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#Data Set
countries=['India', 'Australia',
           'Japan', 'America',
           'Russia']
 
values = [4500, 2500, 1053, 500,
          3200]

#The plot
fig1 = go.Figure(
    go.Pie(
    labels = countries,
    values = values,
    hoverinfo = "label+percent",
    textinfo = "value"
))

st.header("Pie chart")
st.plotly_chart(fig1)

#Donut Chart
import plotly.express as px

    #Data Set
data_frame = {'India': 4500,
              'Australia': 2500,
              'Japan': 1053,
              'America': 500,
              'Russia': 3200  }

fig2 = px.pie(
    hole = 0.2,
    labels = data_frame.values(),
    names = data_frame.keys(),
)

st.header("Donut chart")
st.plotly_chart(fig2)

#Scatter Plot
import numpy as np
value_x = np.random.randint(1, 101, 100)
value_y = np.random.randint(1, 101, 100)

fig3 = px.scatter(
    x = value_x,
    y = value_y,
)

st.header("Scatter Plot")
st.plotly_chart(fig3)

#Line Plot
#import streamlit as st
#import pandas as pd
import plotly.graph_objects as go
    #Data Set
df = pd.DataFrame(dict(
    X_axis = [i for i in range(100)],
    Y_axis = np.random.randint(10, 50, 100)
))

fig4 = px.line(        
        df, #Data Frame
        x = "X_axis", #Columns from the data frame
        y = "Y_axis",
        title = "Line frame"
    )

    #fig.update_traces() function allows us to change visual properties to plot like colour, etc.
fig4.update_traces(line_color = "maroon")
st.header("Line Plot")
st.plotly_chart(fig4)

#Bar Graph
#   Similar to Line Plot, Plotly has express.bar() function to create a bar graph. The bar() function also takes two 
#   list’s as parameters to plot in X, Y axes OR a data set can be mentioned and data set’s columns can be used for 
#   the X & Y axes. There’s an optional parameter called title, a title for the plot.
#   Data Set

#   A Pandas Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
dict = {'X_axis': np.random.randint(10, 50, 20),
            'Y_axis': [i for i in range(20)]}

df = pd.DataFrame(dict)

fig5 = px.bar(        
        df,
        x = "X_axis",
        y = "Y_axis",
        title = "Bar Graph"
    )

st.header("Bar Graph")
st.plotly_chart(fig5)

    #Axis to color
color="X_axis", 

fig6 = px.bar(        
        df,
        x = "X_axis",
        y = "Y_axis",
        title = "Bar Graph",
        color="X_axis",
)
st.plotly_chart(fig6)

#Horizontal Bar Graph

fig7 = px.bar(        
        df,
        x = "X_axis",
        y = "Y_axis",
        title = "Horozontal Bar Graph",
        color="X_axis",
        orientation = 'h' #Optional Parameter
    )

st.plotly_chart(fig7)

#SubPlots in Plotly
#   Subplot enables to load the different plots(i.e bar graph, lin plot) side by side. Figures with subplots are created using 
#   the make_subplots() – function from the plotly.subplots – module.

from plotly.subplots import make_subplots

# Specify number of rows and columns
fig = make_subplots(rows=1, cols=2)

#First SubPlot
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3], 
        y=[4, 5, 6]),
        row=1, col=1
    )

#Second SubPlot
fig.add_trace(
    go.Scatter(
        x=[20, 30, 40], 
        y=[50, 60, 70]),
        row=1, col=2
    )

st.plotly_chart(fig)
st.header("SubPlot")

#Stacked Subplots
# Creating a figure with subplots that are stacked on top of each other since there are 3 rows and 1 column in the subplot layout.

#import streamlit as st
#import pandas as pd
#import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=1)

#First Subplot
fig.add_trace(go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
), row=1, col=1)

#Second SubPlot
fig.add_trace(go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
), row=2, col=1)

#Third SubPlot
fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
), row=3, col=1)

st.plotly_chart(fig)


# Histogram
# import streamlit as st
import plotly.figure_factory as ff
# import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)