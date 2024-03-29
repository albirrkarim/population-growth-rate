# AL BIRR KARIM SUSANTO
# albirkarim1@gmail.com
# https://github.com/albirrkarim/
# http://prajanto.blog.dinus.ac.id/courses/modeling-and-simulation/

# ----------------------- Euler Method ----------------------

from tabulate import tabulate
import numpy as np
import time
start_time = time.time()


# Description
# Growth Function

    # dP / dt = P * r

# Death Function

    # dD / dt = (r * P / M) *P

# M = region capacity

# Delta P = Growth  - Death

# Delta t = 0.5

# Input & Initialize

firstPopulation = 100.0
growthRate      = 0.1
M               = 500.0
deltaT          = 0.5

def GrowthFunc(b):
    return growthRate*b

population      = firstPopulation

results=[]

deltaP=0.0

# Process
for t in np.arange(0, 10, deltaT):
    population=population+(deltaP*deltaT)

    growth=GrowthFunc(population)

    death=growth*(population/M)

    deltaP=growth-death

    results.append((t,population,growth,death,deltaP))



# Measure Time & Heap Memory
print("__________Measurement__________\n")
# Time
print("______Time______\n\n")
end_time = time.time()
delta_time = end_time-start_time
print("Execution Time : ",delta_time," ms\n")

# Memory
print("_____Memory_____\n")
from guppy import hpy
h = hpy()
print (h.heap())


# Output
print(tabulate(results,headers=["t","P(t)","r*P","r*P/M*P","deltaP"],tablefmt="fancy_grid"))
