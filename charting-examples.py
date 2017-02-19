import pylab

def drawGraph(xData,yData):
    pylab.figure(1)
    pylab.plot(xData,yData)
    pylab.title('Age vs. weight for an average boy')
    pylab.xlabel('Age (Months)')
    pylab.ylabel('Weight (lb)')
    #
    pylab.show()

# Data
ageBoys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
weightBoys = [7.16, 9.15, 10.91, 12.56, 14, 15.43, 16.53, 17.64, 18.74, 19.62, 20.28, 21.05, 22, 22.27, 22.82, 23.26, 23.7, 24.14, 24.58, 25.02, 25.35, 25.79, 26.12, 26.57, 28.4]
#
# Call:
drawGraph(ageBoys,weightBoys)


###########################################################################
#
# Next plotting demo...
#
import matplotlib.pyplot as plt

def plotgraph(data):
    plt.plot(data)
    plt.ylabel('some numbers')
    #
    plt.show()

# Data
mydata = [1,2,3,4]
#
# Call:
plotgraph(mydata)
#
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
#
# Default 3rd parameter is b- = solid blue line
#   ro = red circles (syntax from matlab)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
# axis() takes a list of [xmin,xmax,ymin,ymax]
plt.axis([0,6,0,20])
plt.show()


###########################################################################
#
# Next plotting demo...
#
import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


###########################################################################
#
# Next plotting demo...
#
import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
    Bar(
        x=['Pac Man', 'The Legenda of Zelda', 'Doom'],
        y=[15, 11, 3]
    )
])
plot_url = py.plot(data, filename='basic-bar')


###########################################################################
#
# Next plotting demo...
#
"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()


###########################################################################
#
# Horizontal bar chart
#
#import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Example data
games = ('Pac Man','The Legend of Zelda','Doom')
y_pos = np.arange(len(games))
popularity = (15,11,4)

plt.barh(y_pos, popularity, align='center', alpha=0.4)
plt.yticks(y_pos, games)
plt.xlabel('Number of members who like it')
plt.title('Popularity of games liked by members')

plt.show()

