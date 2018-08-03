import matplotlib
matplotlib.use('tkAgg')  # bring upfront

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

leng = 16
for i in range(leng):
    #Data
    datdict = dict()
    datdict['x'] = range(1,11)
    datdict['ya'] = np.random.randn(10)
    datdict['yb'] = np.random.randn(10) + range(1,11)
    datdict['yc'] = np.random.randn(10) + range(11, 21)
    df = pd.DataFrame(datdict)

    # Multiple lines plot
    plt.plot('x', 'ya', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.plot('x', 'yb', data=df, marker='', color='olive', linewidth=2)
    plt.plot('x', 'yc', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
    plt.title("The %s-th PLOT:" % (i + 1))
    plt.legend()
    plt.pause(0.7)
    if i < leng - 1:
        plt.clf() # CLEAR FIGURE
        
plt.show() # HOLD for the last plot
