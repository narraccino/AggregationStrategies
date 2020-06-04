#ISTOGRAMMA


import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [102391, 73753, 39069, 17961, 7245, 3093, 1278, 538, 239, 94, 29, 23, 2, 2, 4]

plt.bar(x,y)

plt.yscale('log', nonposy='clip')
plt.xlabel('Categories in common')
plt.ylabel('Number of POIs')
plt.title('POIs with categories in common')
plt.legend()
fig1= plt.gcf()
plt.show()
plt.draw()
fig1.savefig('poi-Cat.png', dpi=100)


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = [2, 1, 76, 140, 286, 267, 60, 271, 5, 13, 9, 76, 77, 6, 2, 27, 22, 1, 12, 7,
#      19, 81, 11, 173, 13, 7, 16, 19, 23, 197, 167, 1]
# x = pd.Series(x)
#
# # histogram on linear scale
# plt.subplot(211)
# hist, bins, _ = plt.hist(x, bins=8)
#
# # histogram on log scale.
# # Use non-equal bin sizes, such that they look equal on log scale.
# logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
# plt.subplot(212)
# plt.hist(x, bins=logbins)
# plt.xscale('log')
plt.show()