import numpy as np
a = np.array ([3.16, 0.0])
b = np.array 
p = 0.0
q = 0.0
theta = 0.785398
alpha = (np.pi - theta)

def main(): 
    ax = ((a[0]) - p) * np.cos(theta) - ((a[1]) - q) * np.sin(theta) + p
    ay = ((a[0]) - p) * np.sin(theta) + ((a[1]) - q) * np.cos(theta) + q
    return np.array([ax, ay]) 

y = main()
print(y)

#import numpy as np
#
#coordinates = np.array([0.0, 0.0, -3.16, 3.16, -6.32, 0.0, -3.16, -3.16])
# 
#theta = 0.785398
#p = 0.0
#q = 0.0
#
#def main ():
#    i = coordinates[0:7:2]
#    j = coordinates[1::2]
#
#    for i in coordinates:
#            newx = (i - p) * np.cos(theta) - (i - q) * np.sin(theta) + p
#    for j in coordinates:
#            newy = (j - p) * np.cos(theta) - (j - q) * np.sin(theta) + p
#    
#    return newx, newy
#
#y = main()
#print(y)