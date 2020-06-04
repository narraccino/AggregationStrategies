import pickle
import numpy as np

with open('listaIDPOI.pkl', 'rb') as f:
    listaIDPOI = pickle.load(f)
    f.close()

with open('listaIDCAT.pkl', 'rb') as f:
    listaIDCAT = pickle.load(f)
    f.close()

mask = np.load('mask.npy')


print(mask[listaIDPOI.index(152280)][listaIDCAT.index(1535)])

