import numpy as np
X = np.random.random((5,5))
Z = ((X - (X.mean()))/X.std())
print (Z)