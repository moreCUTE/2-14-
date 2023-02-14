
import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')#make the graph polar

#these three lines remove the axes and labels
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)

#lists to hold all the points being plotted
angle = []
radius = []
radius2 = []
radius3 = []
radius4 = []
radius5 = []
radius6 = []

#populate the angle list with a bunch of angles
for i in range(-628,628): #go from negative 2pi to 2pi
     angle.append(i/100)
  
#for each angle, push a radius in to the other list
for i in range(len(angle)):
    radius.append(6*np.cos(angle[i]*12)) #equation is 6*cos(12*angle)
    radius2.append(4*np.cos(angle[i]*8)) #equation is 4*cos(8*angle)
    radius3.append(2*np.cos(angle[i]*4))
    radius4.append(8*np.cos(angle[i]*14))
    radius5.append(3*np.cos(angle[i]*6))
    radius6.append(24*np.cos(angle[i]*22))

plt.plot(angle, radius, color = "blue") #actually draw it
plt.plot(angle, radius2, color = "purple") #actually draw it
plt.plot(angle, radius3, color = "red") #actually draw it
plt.plot(angle, radius4, color = "yellow") #actually draw it
plt.plot(angle, radius5, color = "green") #actually draw it
plt.plot(angle, radius6, color = "black") #actually draw it
plt.show()
