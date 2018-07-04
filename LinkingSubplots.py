import matplotlib
matplotlib.use('tkAgg')

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

def cylinder(r, n):
    '''
    Returns the unit cylinder that corresponds to the curve r.
    INPUTS:  r - a vector of radii
             n - number of coordinates to return for each element in r

    OUTPUTS: x,y,z - coordinates of points
    '''

    # ensure that r is a column vector
    r = np.atleast_2d(r)
    r_rows, r_cols = r.shape

    if r_cols > r_rows:
        r = r.T

# find points along x and y axes
    points = np.linspace(0, 2 * np.pi, n + 1)
    x = np.cos(points) * r
    y = np.sin(points) * r

    # find points along z axis
    rpoints = np.atleast_2d(np.linspace(0, 1, len(r)))
    z = np.ones((1, n + 1)) * rpoints.T

    return x, y, z

#---------------------------------------
# 3D example
#---------------------------------------
fig = plt.figure()

# a background axis to draw lines on
ax0 = plt.axes([0., 0., 1., 1.])
ax0.set_xlim(0, 1)
ax0.set_ylim(0, 1)
# use these to know how to transform the screen coords
dpi = ax0.figure.get_dpi()
height = ax0.figure.get_figheight() * dpi
width = ax0.figure.get_figwidth() * dpi

# top figure
ax1 = fig.add_subplot(2, 1, 1, projection='3d')
x, y, z = cylinder(np.linspace(2, 1, num=10), 40)
for i in range(len(z)):
    ax1.plot(x[i], y[i], z[i], 'c')

# bottom figure
ax2 = fig.add_subplot(2, 1, 2, projection='3d')
x, y, z = cylinder(np.linspace(0, 1, num=10), 40)
for i in range(len(z)):
    ax2.plot(x[i], y[i], z[i], 'r')

# first point of interest
p1 = ([2], [0], [0])
ax1.plot(p1[0], p1[1], p1[2], 'go')
x1, y1, _ = proj3d.proj_transform(p1[0], p1[1], p1[2], ax1.get_proj())
# convert 2d space to screen space
[x1, y1] = ax1.transData.transform((x1[0], y1[0]))
# put them in screen space relative to ax0
x1 = x1 / width
y1 = y1 / height

# another point of interest
p2 = ([1], [0], [1])
ax2.plot(p2[0], p2[1], p2[2], 'go')
x2, y2, _ = proj3d.proj_transform(p2[0], p2[1], p2[2], ax2.get_proj())
# convert 2d space to screen space
[x2, y2] = ax2.transData.transform((x2[0], y2[0]))
x2 = x2 / width
y2 = y2 / height

# plot line between subplots
transFigure = fig.transFigure.inverted()
coord1 = transFigure.transform(ax0.transData.transform([x1, y1]))
coord2 = transFigure.transform(ax0.transData.transform([x2, y2]))
fig.lines = ax0.plot((coord1[0], coord2[0]), (coord1[1], coord2[1]),
                     transform=fig.transFigure, linestyle='dashed')

plt.show()
