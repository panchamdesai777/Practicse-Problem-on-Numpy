#find a 3x3 non singular matrix
import numpy as np

# initialize array A and Identity matrix

B= np.array([[2, 0, -1],[0, 2, -1],[-1, 0, 1]])
I= np.identity(3)
A= 3*I - B
print(A)