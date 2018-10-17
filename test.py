import numpy as np

SIZE = 10

# Create Python's lists
l1 = list(range(SIZE))

print(l1[-5:])
print(l1[-5])
a1 = np.arange(1,10)
a2 = a1.reshape(3,3)
print(a2)

print(a2[:,1])