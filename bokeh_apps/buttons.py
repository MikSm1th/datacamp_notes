import pandas as pd
import numpy as np

from bokeh.io import curdoc, output_file, show
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Slider, Select, Button, CheckboxGroup, RadioGroup, Toggle
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal

button = Button(label = 'press me')

def update():
    #Do something interesting
    return 'Pressed' 

button.on_click(update)

toggle = Toggle(label='Some on/off', button_type='success')
checkbox = CheckboxGroup(labels=['foo','bar','baz'])
radio = RadioGroup(labels=['2000','2010','2020'])

#def callback(active):
    # Active tells which button is active

layout = column(button, toggle, checkbox, radio)
curdoc().add_root(layout)
