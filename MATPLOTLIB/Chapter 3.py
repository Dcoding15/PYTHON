import matplotlib.pyplot as plt
import numpy as np

# Label
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Players Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.suptitle("SPORTS DAY")

plt.grid(c='g',ls='--',lw=0.5)      # axis=x only for x axis and axis=y only for y axis

plt.show()