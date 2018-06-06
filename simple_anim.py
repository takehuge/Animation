"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)        # x-array
line, = ax.plot(x, np.sin(5 * x), linewidth=7, color='blue')


def anima(i):
    line.set_ydata(np.sin(5*x+i/5.0))  # update the data
    print(i)
    return line

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, anima, np.arange(1, 200), init_func=init,
    interval=25, blit=False)

#Install FFMPEG using: brew install ffmpeg
ani.save('sinewave.mp4', fps=15)

plt.show()
