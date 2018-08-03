import matplotlib
import time
matplotlib.use('tkAgg')  # bring upfront

# from pylab import linspace, pause
import matplotlib.pyplot as plt
#   plot 0     plot 1    plot 2   plot 3
x = [[1, 2, 3, 4], [1, 4, 3, 4], [1, 2, 3, 4], [9, 8, 7, 4]]
y = [[3, 2, 3, 4], [3, 6, 3, 4], [6, 7, 8, 9], [3, 2, 2, 4]]

plots = zip(x, y)


def loop_plot(plots):
    figs = {}
    axs = {}
    for idx, plot in enumerate(plots):
        figs[idx] = plt.figure()
        axs[idx] = figs[idx].add_subplot(111)
        axs[idx].plot(plot[0], plot[1])
        plt.pause(3.5)
        plt.close()

    return figs, axs


figs, axs = loop_plot(plots)
# plt.show()
