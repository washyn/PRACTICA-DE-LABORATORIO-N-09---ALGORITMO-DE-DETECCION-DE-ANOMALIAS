import numpy as np
import math
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
    [4,8,6],
    [4,8,6],
    [4,8,6],
    [4,8,6]
]


# datos[0:,0]
d = np.array(datos)

# recibira una col
# [5,5,5,8,5,2,8,8,5,]
def get_u2(x_i):
    m = len(x_i)
    return np.sum(x_i)/m

def get_u(x_i):
    return np.mean(x_i)

# recibira una columna
def get_sigma(x_i ,u_i):
    m = len(x_i)
    return np.sum((x_i - u_i)**2)/m
    

# # version larga de sigma
# def get_sigma2():
#     m = len(x_i)
#     sumatoria = 0
#     for j in range(m):
#         sumatoria += (x_i[j] - u_i)**2
#     return sumatoria/m



def p(x, u, sigma):
    ex = (-1) * ((x - u)**2)/(2 * sigma)
    return np.exp(ex) / np.sqrt((2 * np.pi * sigma))   


# m = cantidad de muestras
m = len(d)
# n = cantidad de caracteristicas
n = len(d[0])

# u = [get_u(d[:,i]) for i in range(n)]
# sigma = [get_sigma(d[:,i], u[i]) for i in range(n)]
sigma = [get_sigma(d[:,column_i], get_u(d[:,column_i])) for column_i in range(n)]



# debo tener los u, y los sigmas...

for i in range(n):
    # print(p(d[:,i]))
    pass

# math.exp(2)
# 7.38905609893065
# np.exp(2)
# 7.38905609893065