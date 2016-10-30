import pandas as pd
import numpy as np
from matplotlib import pylab as plt
import random
import math

x = np.array([-5.12, 5.12])
n = 5 #number parents in population
size_x = 3
F = random.random() * 2 #value of parameter F [0, 2]
CR = random.random() #crossover rate


#function
def f(*args):
    suma = 0
    for i in args:
        suma += i ** 2
    return suma

#function for array
def func(*args):
    suma = 0
    array = args[0]
    for i in array:
        suma += i ** 2
    return suma

#draw graph of function
def draw_graph(rangex = [-5.12, 5.12], rangey =[-2, 30], name="graph",title="x1^2 + x2^2 + x3^2", xlabel="x", ylabel="y", points_x=[]):
    plt.ion()
    x1 = np.arange(rangex[0], rangex[1] + 0.1, 0.1)
    x2 = x3 = x1

    y = np.array(f(x1, x2, x3))
    plt.plot(x1, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis([rangex[0], rangex[1], rangey[0], rangey[1]])

    if points_x != []:
        points_y = np.array(f(points_x))
        plt.scatter(points_x, points_y, color="red")
    plt.savefig(name + ".png")
    plt.ioff()
    plt.show()

#initialize array
def initialize():
    init = np.zeros([n, size_x])
    for i in range(n):
        for j in range(size_x):
            init[i, j] = x[0] + random.random()*(x[1] - x[0])
    return init

#make mutation
def make_mutation(xi):
    pop = np.array([x for x in range(3)])
    mut = np.zeros([n, size_x])
    rangeg = range(n)
    for i in range(n):
        flag = False
        while not flag:
            pop = np.array(random.sample(rangeg, 3))
            flag = True
            for k in range(2):
                if not flag:
                    break
                for j in range(i+1, 3):
                    if pop[k] == i or pop[j] == i:
                        flag = False
                        break
        for k in range(size_x):
            mut[i, k] = xi[pop[0]][k] + F * (xi[pop[1]][k] - xi[pop[2]][k])
    return mut

#make crossover
def make_crossover(xi, vi):
    crossover = np.array(vi)
    flag = True
    for i in range(n):
        if random.random() <= CR:
            flag = False
        else:
            crossover[i] = xi[i]
    if flag:
        i = random.randint(0, n-1)
        crossover[i] = xi[i]
    return crossover

#minimize
def choose(xi, ui):
    new_population = np.array(xi)
    for i in range(n):
        if func(ui[i]) < func(xi[i]):
            new_population[i] = ui[i]
    return new_population

#algorithm
def do():
    x0 = initialize()
    print(x0)
    array = np.array([func(x) for x in x0])
    print(array)
    for i in range(500000):
        vi = make_mutation(x0)
        ui = make_crossover(x0, vi)
        x0 = choose(x0, ui)
    array = np.array([func(x) for x in x0])
    print(CR, F)
    print(x0)
    print(min(array))

#result
if __name__=="__main__":
    #draw_graph()
    do()