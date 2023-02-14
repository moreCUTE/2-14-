import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')

#these three lines remove the axes and labels
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)

#lists to hold all the points being plotted
angle = []
radius = []

#populate the angle list with a bunch of angles
for i in range(-314, 314): #go from negative pi to pi
     angle.append(i/100)
  
#for each angle, push a radius in to the other list
radius = 1-np.sin(angle)

plt.plot(angle, radius, color = 'pink') #actually draw it
plt.plot(angle, radius*2, color ='red') #actually draw it
plt.plot(angle, radius*3, color ='blue') #actually draw it
plt.plot(angle, radius/2, color ='purple') #actually draw it
plt.show()

