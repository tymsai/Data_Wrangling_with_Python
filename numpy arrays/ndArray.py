#nd arrays numpy
import numpy as np
list2d=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat1=np.array(list2d)
print(type(mat1))
print("Matrix :\n", mat1)
print("Dimensions : ", mat1.ndim)
print("size of matrix : ", mat1.size)
print("Shape of matrix : ", mat1.shape)
print("Data type of elements : ", mat1.dtype)

mat2=mat1*mat1
print(mat2)

