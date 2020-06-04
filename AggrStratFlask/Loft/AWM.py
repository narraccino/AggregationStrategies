import pandas as pd
from collections import OrderedDict
from IPython.display import display
from IPython.display import Image
import copy

def getKeys(raw_data, threshold):

    dataset = copy.deepcopy(raw_data)

    for key, value in raw_data.items():
        if (min(value) < threshold):
            del dataset[key]

    colonne= list(dataset.keys())

    return colonne

def averageWithoutMisery(raw_data):
    dataset = copy.deepcopy(raw_data)
    for key, value in dataset.items():
        somma = sum(value)
        dataset[key] = somma
    return dataset
