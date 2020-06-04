import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image




def mostPleasure(raw_data):

    for key, value in raw_data.items():
        maximo= max(value)
        raw_data[key]=maximo

    return raw_data
