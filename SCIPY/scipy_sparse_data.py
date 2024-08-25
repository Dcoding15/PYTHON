import scipy.sparse as spc
import numpy as np

'''

Sparse Data - It is a data set where most of items value zero
There are primarily two types of square matrices: -
    1. CSC - Compressed Sparsed Column
    2. CSR - Compressed Spared Row
'''

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(spc.csr_matrix(arr))