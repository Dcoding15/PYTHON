# Matplotlib - low level graph plotting library

#Pyplot
import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([0,10])
y_axis = np.array([1,100])

plt.plot(x_axis,y_axis)         # Normal plotting
plt.show()

plt.plot(x_axis,y_axis,'o')     # Plotting without line
plt.show()

x_axis = np.array([1,2,6,8])
y_axis = np.array([3, 8, 1, 10])

plt.plot(x_axis,y_axis)           # Multiple plotting
plt.show()

plt.plot(y_axis)                  # Default x-axis plotting
plt.show()

plt.plot(x_axis)                  # Default x-axis plotting
plt.show()