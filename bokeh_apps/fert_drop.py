import pandas as pd
import numpy as np

from bokeh.io import curdoc, output_file, show
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Slider, Select
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal


df = pd.read_csv('literacy_birth_rate.csv', skipfooter = 20)
female_literacy = np.array(df['female literacy']).astype('float')
fertility = np.array(df['fertility']).astype('float')
population = np.array(df['population']).astype('float')

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)