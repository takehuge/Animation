import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
fig=plt.figure()
fig.canvas.manager.window.attributes(
    '-topmost', 1)  # stay on top of all windows
fig.canvas.manager.window.attributes(
    '-topmost', 0)
