from tqdm import tqdm
import time
import itertools


pbar = tqdm(total=1000)
for i in range(1000):
    pbar.update(1)
    time.sleep(0.5)
pbar.close()