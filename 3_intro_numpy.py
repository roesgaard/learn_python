"""
NumPy
--------------------------------------------------------------------------
A fundamental package for numerical manipulations
For list of functions look here:
    https://numpy.org/doc/stable/reference/routines.math.html
""" 
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum
print(x + y)
print(np.add(x, y))

# Elementwise difference
print(x - y)
print(np.subtract(x, y))

# Elementwise product
print(x * y)
print(np.multiply(x, y))

# Elementwise division
print(x / y)
print(np.divide(x, y))

# Elementwise square root
print(np.sqrt(x))

# ELementwise sum
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

# More advanced
a1 = np.arange(10,14)
a2 = np.arange(20,24)
a12 = np.concatenate((a1,a2))
print(a1)
print(a2)
print(a12)
a = np.concatenate((a12,20+a1))
print(a)
print(a.shape)

# transform it to two-dimensional NumPy array
a = a.reshape(3,4)
print(a)
print(a.shape)

# index an array
print(a[0])
print(a[0][2])

print(a[:,2])

# transposed, meaning that rows and coloumns are interchanged
print(np.transpose(a))