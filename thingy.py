import numpy as np
import matplotlib.pyplot as plt
pi = 3.1415

plt.axes(projection = 'polar')

#lists to hold all the points being plotted
angle = [0, pi/2, 7*pi/4, pi, 3*pi/2, 2*pi, 5*pi/1]
radius = [1, 2, 5, 3, 4, 5, 6]
print(angle, radius) # see numbers that are being drawn

plt.plot(angle, radius, color = 'green') #actually draw it

plt.show()
