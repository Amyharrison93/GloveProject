'''
library to simplify the use of graphing libraries found in python
'''

#import matplotlib
#matplotlib.use('Agg')
from matplotlib.pyplot import plot, show, figure
from matplotlib.animation import FuncAnimation
from matplotlib import style
from numpy import array

style.use('fivethirtyeight')

fig = figure()
ax1 = fig.add_subplot(1,1,1)

def TestPlot():
    # X axis parameter:
    xaxis = array([2, 8])

    # Y axis parameter:
    yaxis = array([4, 9])

    plot(xaxis, yaxis)
    show()
    
def plotPoints2d(points):
    '''plots points onto a dynamic graph
    input is an array of points to be plotted only 2 dimentions required'''
    
    xpoints = points[0]
    ypoints = points[1]
    
    plot(xpoints, ypoints, 'o')
    show()
    
def plotPoints3d(points):
    '''plots points onto a dynamic graph
    input is an array of points to be plotted only 2 dimentions required'''
    
    xpoints = points[0]
    ypoints = points[1]
    zpoints = points[2]
    
    plot(xpoints, ypoints, zpoints, 'o')
    show()
    
def animate(data):
    xs = data[0]
    ys = data[1]
    ax1.clear()
    ax1.plot(xs, ys)
    
    ani = FuncAnimation(fig, animate, interval=1000)
    show()