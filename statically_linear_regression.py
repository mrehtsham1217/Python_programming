import matplotlib.pyplot as plt
%matplotlib inline
from scipy import stats
import numpy as np

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

slope,intercept,r,p,std_err= stats.linregress(x,y)
print(r)
print(p)
print(std_err)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x,mymode)
plt.show()
