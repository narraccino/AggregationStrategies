import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image



def leastMisery(raw_data):

    for key, value in raw_data.items():
        minimo= int(min(value))
        raw_data[key]=minimo
    return raw_data

