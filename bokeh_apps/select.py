import pandas as pd
import numpy as np

from bokeh.io import curdoc, output_file, show
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Slider, Select
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal

N = 1000
source = ColumnDataSource(data={'x': random(N), 'y': random(N)})

# Create plot and widgets

plot = figure()
plot.circle(x='x', y='y', source=source)

menu = Select(options=['uniform', 'normal', 'lognormal'],
                value='uniform', title='Distribution')

def callback(attr, old, new):
    if      menu.value == 'uniform': f = random
    elif    menu.value == 'normal':  f = normal
    else:                            f = lognormal
    source.data = {'x': f(size=N), 'y': f(size=N)}

menu.on_change('value', callback)

layout = column(menu, plot)

curdoc().add_root(layout)