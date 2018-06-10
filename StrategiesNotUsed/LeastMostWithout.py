from LM import leastMisery
from MP import mostPleasure
from AWM import getKeys, averageWithoutMisery
from utility import mergeDictionaries, match, orderList
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


df_a = pd.DataFrame(raw_data,columns = ['A', 'B','C','D','E','F','G','H','I','J'])
print(df_a, '\n')



data1 = copy.deepcopy(raw_data)
new_list1= leastMisery(data1)


data2 = copy.deepcopy(raw_data)
new_list2= mostPleasure(data2)

chiavi= getKeys(raw_data,threshold)

new_list3 = mergeDictionaries(new_list1, new_list2)

new_list4= match(chiavi, new_list3)

defList= averageWithoutMisery(new_list4)


print("The sequence is: ")
ordDf= orderList(defList)