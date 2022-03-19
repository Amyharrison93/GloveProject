import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np

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