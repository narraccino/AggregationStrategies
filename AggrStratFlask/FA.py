import pandas as pd
import numpy as np
import itertools


def FairenessAverage(ratingsArraylist, list_POI, list_Names):
    class Engine(object):

        def __init__(self, num):
            self.index = 0

        def valueReturn(self, lista):
            letter = lista[self.index]
            self.index = self.index + 1
            return letter

    final_list = list()


    ratingsArrayPOI = np.array(ratingsArraylist)

    obj = []
    for i in range(len(list_Names)):
        obj.append(Engine(i))

        # creo un dataframe a partire dai ratings degli utenti
        unsorted_df = pd.DataFrame(ratingsArrayPOI, columns=list_POI)

        # aggiungo al dataframe la riga "Total"
        somma = unsorted_df.sum()
        unsorted_df.loc['Total'] = unsorted_df.sum()

    for i in range(0, len(list_Names)):

        # ordino le colonne a partire dalla riga 0 mediante ratings. Otterrò la riga i-esima ordinata
        row = unsorted_df.sort_values(by=i, ascending=False, axis=1)

        # allego alla riga i-esima ordinata la riga somma.
        row = row.append(somma, ignore_index=True)

        # creo due liste vuote
        final_list1 = list()
        flattened_list = list()

        for n in range(10, -1, -1):
            # All'interno del dataframe row(compreso di somma), alla riga i-esima ,
            # trova tutte le occorrenze nel numero n.
            # se viene trovato il numero n allora verrà estratta la riga che conterrà solo quelle occorrenze n
            # e per il resto NaN
            vari = row.loc[i, :].where(row.loc[i, :] == n)

            # converte la riga "vari" trasformando i numeri trovati in TRUE e i NaN in FALSE
            bi = vari.notnull()

            # nella riga contenente TRUE e FALSE, estrare i nomi delle colonne e le trasforma in una lista
            columns = bi.index[bi[0:] == True].tolist()

            # se la lista columns non è vuota
            if columns != []:
                # Creo il dataframe df1 che conterrà SOLO le colonne determinate da columns
                df1 = pd.DataFrame(row, columns=columns)

                # Ordino le colonne in base ai valori discendenti di somma che si trovano sull'ultima riga, ovvero 3
                df1 = df1.sort_values(by=len(list_Names), ascending=False, axis=1)

                # prendo le colonne ordinate e le converto in lista
                columns = df1.columns.tolist()

                # aggiungo la lista columns alla lista final
                final_list1.append(columns)

                # faccio in modo che tutti gli elementi siano separati e perciò resi iterabili
                final_list2 = list(itertools.chain.from_iterable(final_list1))

        # aggiungo per ogni iterazione(0-users_number le proprie liste finali ordinate)
        final_list.append(final_list2)

    # print(final_list)
    # print("\n")

    # creo la lista vuota ultimate che sarà quella definitiva
    ultimate = list()

    # indico il numero di spostamenti max che si devono verificare nel momento
    # in cui nel vettore vi sono già lettere scelte in precedenza
    repetition = 2

    # cicla fin quando la lunghezza di ultimate non raggiunge la lunghezza dei POI
    while len(ultimate) != len(list_POI):
        for i in range(0, len(list_Names)):
            # estraggo la i-esima lista ordinata
            lista = final_list[i]

            # valueReturn mi tirerà fuori la lettera in base alla lista passata
            letter = obj[i].valueReturn(lista)

            # se la lettera non è in ultimate allora verrà aggiunta ad ultimate
            if (letter not in ultimate):
                ultimate.append(letter)

            # se i=MAX degli utenti, in questo caso 3 (cioè indice 2) è il max
            if (i == len(list_Names) - 1):
                # arrivato alla fine comincio a fare il conto, perché
                # essendo l'ultimo a scegliere, l'algoritmo riparte dall'ultimo utente
                # e itera sulla lista di "confine" da 0 fino al numero max di ripetizioni
                for k in range(0, repetition - 1):
                    letter = obj[i].valueReturn(lista)
                    if (letter not in ultimate):
                        ultimate.append(letter)

                # comincio a tornare indietro fino al "confine" inizio
                for j in range(len(list_Names) - ((len(list_Names) - 1)), -1, -1):
                    lista = final_list[j]
                    letter = obj[j].valueReturn(lista)
                    if (letter not in ultimate):
                        ultimate.append(letter)

                # arrivato di nuovo al punto di partenza comincio a fare il conto, perché
                # essendo l'ultimo a scegliere, l'algoritmo riparte di nuovo dal primo utente
                # e itera sulla lista di "confine" da 0 fino al numero max di ripetizioni
                if (j == 0):
                    for k in range(0, repetition - (len(list_Names) - 1)):
                        letter = obj[j].valueReturn(lista)
                        if (letter not in ultimate):
                            ultimate.append(letter)

    #print(ultimate)

    return ultimate
