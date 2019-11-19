import numpy as np
x = np.arange(1,101,1)
x = x.reshape(10,10)
xs = np.square(x)
xz=xs[xs%3==0]
print (xz)