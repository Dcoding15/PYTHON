import matplotlib.pyplot as plt
import numpy as np

# Marker

x_axis = np.array([1,2,6,8])
y_axis = np.array([3, 8, 1, 10])

plt.plot(x_axis,y_axis,'^-r',ms=10,mec='b',mfc='g')     # ms -> markersize; mec -> markeredgecolor; mfc -> makerfacecolor
plt.show()

# Line
plt.plot(y_axis,ls='dotted', c='r', lw=5)  # ls means linestyle; c means color; lw means linewidth
plt.show()

'''

marker|line|color

marker: -
o   --> Circle	
*   --> Star	
.   --> Point	
,   --> Pixel	
x   --> X	
X   --> X (filled)	
+   --> Plus	
P   --> Plus (filled)	
s   --> Square	
D   --> Diamond	
d   --> Diamond (thin)	
p   --> Pentagon	
H   --> Hexagon	
h   --> Hexagon	
v   --> Triangle Down	
^   --> Triangle Up	
<   --> Triangle Left	
>   --> Triangle Right	
1   --> Tri Down	
2   --> Tri Up	
3   --> Tri Left	
4   --> Tri Right	
|   --> Vline	
_   --> Hline

line: -
-   --> Solid line	
:   --> Dotted line	
--  --> Dashed line	
-.  --> Dashed/dotted line

color: -
r   --> Red	
g   --> Green	
b   --> Blue	
c   --> Cyan	
m   --> Magenta	
y   --> Yellow	
k   --> Black	
w   --> White

'''