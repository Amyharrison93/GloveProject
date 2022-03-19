#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def TestPlot():
    # X axis parameter:
    xaxis = np.array([2, 8])

    # Y axis parameter:
    yaxis = np.array([4, 9])

    plt.plot(xaxis, yaxis)
    plt.show()
    
def plotPoints2d(points):
    '''plots points onto a dynamic graph
    input is an array of points to be plotted only 2 dimentions required'''
    
    xpoints = points[0]
    ypoints = points[1]
    
    plt.plot(xpoints, ypoints, 'o')
    plt.show()
    
def plotPoints3d(points):
    '''plots points onto a dynamic graph
    input is an array of points to be plotted only 2 dimentions required'''
    
    xpoints = points[0]
    ypoints = points[1]
    zpoints = points[2]
    
    plt.plot(xpoints, ypoints, zpoints, 'o')
    plt.show()
    
def animate(data):
    xs = data[0]
    ys = data[1]
    ax1.clear()
    ax1.plot(xs, ys)
    
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()