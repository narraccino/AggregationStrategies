from Loft.LM import leastMisery
import pandas as pd
import copy
threshold=4


raw_data = {
        'A': [10,1,10],
        'B': [4,9,5],
        'C': [3,8,2],
        'D': [6,9,7],
        'E': [10,7,9],
        'F': [9,9,8],
        'G': [6,6,5],
        'H': [8,9,6],
        'I': [10,3,7],
        'J': [8,8,6],

}

data1 = copy.deepcopy(raw_data)
new_list1= leastMisery(data1)
