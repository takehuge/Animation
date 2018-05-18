"""
Simple demo with multiple subplots.
"""
import numpy as np
import Fig_Show # put before importing another matplotlib modules
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'ko-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
# plt.show()
plt.show(block=False) # allow later fig to spawn w/o have to close this one!

# display this plot as well together with previous one
plt.figure(2)
plt.plot(np.arange(0, 10, 1), np.arange(0, 20, 2))
plt.show(block=False)

plt.ioff()
plt.figure(3)
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
