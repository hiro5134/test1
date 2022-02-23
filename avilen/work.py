import numpy as np

a = np.arange(24).reshape(2,3,4)

b = a - 12
c = np.arange(24).reshape(2,4,3)

print(a)
print(b)
print(c)

print("dot", np.dot(a,c))

#アダマール積
print("times", a*b)
