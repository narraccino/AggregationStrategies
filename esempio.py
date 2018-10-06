import pandas as pd
import numpy as np

def deleteExcept(answ,nQuest,df):
    nQuest = nQuest - 1

    if(answ == 'A'):
        df_a = df.loc[nQuest]
        df_a[df_a[:] == 'B'] = 0
        df.loc[nQuest] = df_a


    else:
        df_a = df.loc[nQuest]
        df_a[df_a[:] == 'A'] = 0
        df.loc[nQuest] = df_a

def showBehaviour(lista):
    print("Competing: ")
    print(lista[0])
    if (0 <=lista[0]<=3):
        print("25%")
    if (4 <=lista[0]<=7):
        print("50%")
    if (8 <= lista[0] <= 12):
        print("75%")

    print("Collaborating: ")
    print(lista[1])
    if (0 <= lista[1] <= 5):
        print("25%")
    if (6 <= lista[1] <= 9):
        print("50%")
    if (10 <= lista[1] <= 12):
        print("75%")

    print("Compromising: ")
    print(lista[2])
    if (0 <= lista[2] <= 4):
        print("25%")
    if (5 <= lista[2] <= 8):
        print("50%")
    if (9 <= lista[2] <= 12):
        print("75%")

    print("Avoiding: ")
    print(lista[3])
    if (0 <= lista[3] <= 4):
        print("25%")
    if (5 <= lista[3] <= 7):
        print("50%")
    if (8 <= lista[3] <= 12):
        print("75%")

    print("Accomodating: ")
    print(lista[4])
    if (0 <= lista[4] <= 3):
        print("25%")
    if (4 <= lista[4] <= 6):
        print("50%")
    if (7 <= lista[4] <= 12):
        print("75%")



risposte = list()

infile = open('questions.txt', 'r')

for i in range(0,30):
    lineA = infile.readline()
    lineB = infile.readline()

    print("Question Number " + str(i))
    print('A. ' + lineA)
    print('B. ' + lineB)

    lineBlank= infile.readline()
    ris=input('Choose A or B ')
    risposte.append(ris)



df= pd.read_excel('tkitable.xlsx')

i=1
for answ in risposte:
    deleteExcept(answ,i,df)
    i=i+1


df = df.replace(0, np.nan)
print(df)
df_b = df.count()
list_a= df_b.tolist()
showBehaviour(list_a)






