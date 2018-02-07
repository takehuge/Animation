from numpy import *
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# our equilateral triangle vertices
v1 = [0,0]
v2 = [1,0]
v3 = [0.5,sqrt(3)/2]

# initial values
xdata, ydata = [], []

fig, ax = plt.subplots()
line, = ax.plot([], [],'m.',markersize=3)
ax.set_ylim(0, sqrt(3)/2)
ax.set_xlim(0, 1)
#ax.grid()

def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]

def data_gen():
    x = data_gen.x
    y = data_gen.y
    count = data_gen.count
    curr_point = [x,y]
    while count < 1000:
        count+=1
        print(count)
        print(curr_point)
        val = randint(0,2)
        print(val)
        if val == 0:
            curr_point = midpoint(curr_point, v1)
        if val == 1:
            curr_point = midpoint(curr_point, v2)
        if val == 2:
            curr_point = midpoint(curr_point, v3)
        x=curr_point[0]
        y=curr_point[1]
        yield x,y

data_gen.x = 0
data_gen.y = 0
data_gen.count = 0

def run(data):
    x,y=data
    xdata.append(x)
    ydata.append(y)   
    line.set_data(xdata,ydata)
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10, repeat=False)  
# set blit=False in Mac
plt.show()

    
    
    