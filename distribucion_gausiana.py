import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

datos = [
# caractertica_1 = c1
# caractertica_2 = c2
# caractertica_2 = c3
# +--+--+--+
# |c1|c2|c3|
# +--+--+--+
# |  |  |  |
# |  |  |  |
# |  |  |  |
# |  |  |  |
# +--+--+--+
    [1,8,6],
    [5,7,5],
    [4,9,4],
    [3,2,9]
]


# datos[0:,0]
x = np.array(datos)
datos = pd.read_csv("F:\\lab de IA\\petrologydata.csv")
x = np.array(datos.values)

# # version larga de sigma
# def get_sigma2():
#     m = len(x_i)
#     sumatoria = 0
#     for j in range(m):
#         sumatoria += (x_i[j] - u_i)**2
#     return sumatoria/m

# recibira una col
# [5,5,5,8,5,2,8,8,5,]
# def get_u2(x_i):
#     m = len(x_i)
#     return np.sum(x_i)/m


def get_u(x_i):
    return np.mean(x_i)

# recibira una columna
def get_sigma(x_i ,u_i):
    m = len(x_i)
    return np.sum((x_i - u_i)**2)/m


# x_j, u_j, sigma_j
def __p(x, u, sigma):
    ex = (-1) * ((x - u)**2)/(2 * sigma)
    return np.exp(ex) / np.sqrt((2 * np.pi * sigma))   


# def p()
#     n = algo
#     res = 1
#     for j in range(n):
        

# m = cantidad de muestras
m = len(x)
# n = cantidad de caracteristicas
n = len(x[0])


# debo tener los u, y los sigmas...
# el promedio de cada columna
u = [get_u(x[:,j]) for j in range(n)]


# sigma = [get_sigma(x[:,column_i], get_u(x[:,column_i])) for column_i in range(n)]
# 
sigma = [get_sigma(x[:,j], u[j]) for j in range(n)]



for j in range(n):
    for i in range(m):
        print(__p(x[i,j], u[j], sigma[j]))
    # print()
#     print(__p(x[:,j], u[j], sigma[j]))
#     print()
#     print(x[:,i])
#     pass
# math.exp(2)
# 7.38905609893065
# np.exp(2)
# 7.38905609893065