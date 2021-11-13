import numpy as np
from numpy import cos as c, sin as s
import random
import math


def get_xyz(t1, d1, d2, d3, t4, t5, t6, d6):
    # for indexes x is the vertical and y the horizontal
    m1 = np.array([ [c(t1), 0,  -s(t1),   -s(t1)*d1], 
                    [s(t1), 0,   c(t1),    c(t1)*d3], 
                    [0,    -1,       0,     d1 + d2], 
                    [0,     0,       0,           1]])

    m2 = np.array([ [c(t4)*c(t5)*c(t6) - s(t4)*s(t6), -c(t4)*c(t5)*s(t6) - s(t4)*c(t6), c(t4)*s(t5), c(t4)*s(t5)*d6],
                    [s(t4)*c(t5)*c(t6) + c(t4)*s(t6), -s(t4)*c(t5)*s(t6) + c(t4)*c(t6), s(t4)*s(t5), s(t4)*s(t5)*d6],
                    [                   -s(t5)*c(t6),                      s(t5)*c(t6),       c(t5),       c(t5)*d6],
                    [                              0,                                0,           0,              1]])

    m3 = np.multiply(m1, m2)
    dx = m3[0, 3]
    dy = m3[1, 3]
    dz = m3[2, 3]
    return [dx, dy, dz]

def dist(cur, goal):
    return math.dist(cur, goal)

def get_random_draw(quenching = 60.0):
    ran = random.random() - 0.5
    ran = ran/quenching
    return ran
    
iterLimit = 5000000
goal = [1.2, .8, .5]
tolerence = .005
traveled = np.zeros(shape=8)
positions = {}

for j in range(8):
    ot1 = t1 = np.radians(-90)
    od1 = d1 = .25
    od2 = d2 = 0.5
    od3 = d3 = 1.0
    ot4 = t4 = np.radians(-90)
    ot5 = t5 = np.radians(90)
    ot6 = t6 = np.radians(40)
    od6 = d6 = 5 

    curPos = get_xyz(t1, d1, d2, d3, t4, t5, t6, d6)

    for i in range(iterLimit):
        t1Temp = t1 + get_random_draw()
        d2Temp = d2 + get_random_draw()
        d3Temp = d3 + get_random_draw() 
        t4Temp = t4 + get_random_draw()
        t5Temp = t5 + get_random_draw()
        t6Temp = t6 + get_random_draw()

        newPos = get_xyz(t1Temp, d1, d2Temp, d3Temp, t4Temp, t5Temp, t6Temp, d6)
        if dist(curPos, goal) > dist(newPos, goal) and random.random() < .9:
            curPos =  newPos
            t1 = t1Temp
            d2 = d2Temp
            d3 = d3Temp
            t4 = t4Temp
            t5 = t5Temp
            t6 = t6Temp
        else:
            pass

        if dist(curPos, goal) < tolerence:
            traveled[j] = t1 - ot1 + d1 - od1 + d2 - od2 + d3 - od3 + t4 - ot4 + t5 - ot5 + t6 - ot6 + d6 - od6
            positions[j] = [t1, d1, d2, d3, t4, t5, t6, d6]
            break

mini = np.inf
posi = 0
for k in range(len(traveled)):
    if traveled[k] < mini:
        mini = traveled[k]
        posi = k
print(positions[posi])
print(traveled[posi])
