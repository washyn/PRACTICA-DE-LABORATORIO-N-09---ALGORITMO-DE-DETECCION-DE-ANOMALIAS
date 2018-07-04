# librerias para manejo de matrices
# para fuciones matematicas
# para leer archivos csv(analisis de datos)
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt



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


def f_u(x_i):
    return np.mean(x_i)

# recibira una columna
def f_sigma(x_i ,u_i):
    m = len(x_i)
    return np.sum((x_i - u_i)**2)/m


# x_j, u_j, sigma_j
def __p(x, u, sigma):
    ex = (-1) * ((x - u)**2)/(2 * sigma)
    return np.exp(ex) / np.sqrt((2 * np.pi * sigma))   


def p1(x, u, sigma, m, n):
    res = np.ones(m)
    for j in range(n):
        res *= __p(x[:,j],u[j],sigma[j])
    return res


def p(x):
    # m = cantidad de muestras
    # n = cantidad de caracteristicas
    m, n = x.shape
    print("m = {}\nn = {}".format(m,n))
    # los u, y los sigmas... antes
    # el promedio de cada columna
    u = [f_u(x[:,j]) for j in range(n)]
    print("u:",u)
    # el sigma para cada columna
    sigma = [f_sigma(x[:,j], u[j]) for j in range(n)]
    print("sigma:",sigma)
    # resultado de la funcion p(x)
    result = p1(x, u, sigma, m, n)
    # print("p(x):",result)
    # mostrar los resultados de la funcion p(x)
    for i in result:
        print("%f"%i)
    return result



def main():
    # caractertica_1 = c1
    # caractertica_2 = c2
    # caractertica_2 = c3
    #             +--+--+--+
    #             |c1|c2|c3|
    #             +--+--+--+
    # sujeto 1    |  |  |  |
    # sujeto 2    |  |  |  |
    # sujeto 3    |  |  |  |
    # sujeto 4    |  |  |  |
    #             +--+--+--+

    datos = [
        # anomalo
        [1,3,11],
        # normal
        [4,8,6],
        [5,7,5],
        [4,9,4],
        [3,7,7]
    ]
    # nuevo_ejemplo = [1,3,11]
    x = np.array(datos)
    # datos = pd.read_csv("F:\\lab de IA\\petrologydata.csv")
    # x = np.array(datos.values)
    res = p(x)


    # epsilon = 0.0005
    # para [1,3,11] el elemento p[0,:]
    # p(x) = 0.000067
    # 0.000067 < 0.0005 
    # True
    # podemos decir que existe anomalia para esta muestra
    # a simple vista se puede ver que esta fila(tupla) tiene valores muy diferentes a los de su columna

    # para [4,8,6] el elemento p[1,:]
    # p(x) = 0.007023
    # 0.007023 < 0.0005 
    # false
    # esta muestra no presenta anomalias, los valores de esta fila(tupla) son similares a las demas muestas no hay una gran diferencia




if __name__ == '__main__':
    main()

    # m = 5
    # n = 3
    # u: [3.4, 6.8, 6.6]
    # sigma: [1.8399999999999999, 4.16, 5.84]
    # 0.000067
    # 0.007023
    # 0.003786
    # 0.002698
    # 0.008926