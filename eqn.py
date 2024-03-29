#solving Equations with numpy
# Code starts here
import numpy as np

# initialize matrix A and b
A= np.array([[2,1,2],[3, 0, 1],[1, 1, -1]])
b= np.array([-3, 5, 2])

# Solve for x
x = np.linalg.solve(A,b)
print(x)

# Check solution

check = np.allclose(np.dot(A,x),b)
print(check)