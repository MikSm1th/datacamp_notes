import pandas as pd
import numpy as np

from bokeh.io import curdoc, output_notebook, show
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from numpy.random import random

df = pd.read_csv('y.csv', header=None, dtype=np.float, usecols=[0,1,2,3,4])

plot=figure()
x = np.linspace(0.3, 10, 300)
y = df.values.flatten()

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x','y', source=source)

slider = Slider(start=1, end=10, value=1,
               step=1, title='scale')

def callback(attr, old, new):
    scale = slider.value
    new_y = np.sin(scale/x)
    source.data={'x': x, 'y': new_y}
    
slider.on_change('value', callback)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)