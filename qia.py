# -*- coding: utf-8 -*-
"""QIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e3JplvpMLyz47QUMBt2qltIMz9C1oY3Y
"""

import quantum_inspired as qi
import numpy as np

# load a low-rank random matrix A with dimension 500 x 250
A = np.load('A.npy')
# load b vector (500 x 1) defining linear system Ax=b
b = np.load('b.npy')
# rank of matrix A
rank = 3
# Input parameters for the quantum inspired algorithm
r = 200
c = 200
Nsamples = 50
NcompX = 50
sampled_comp, x = qi.linear_eqs(A, b, r, c, rank, Nsamples, NcompX)

print(x)

