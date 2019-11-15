import math 
import numpy as np 
            
t = np.linspace(0,100,101)            

angles_1 = []
angles_2 = []


for i in t :

    angle1 = math.sin(i)*-1/5
    angle2 = math.cos(i)*-1/5
    angles_1.append(angle1)
    angles_2.append(angle2)

max1 = max(angles_1)
max2 = max(angles_2)
min1 = min(angles_1)
min2 = min(angles_2)

if max1 <= 0.45 and abs(min1) <= 0.45 and max2 <= 0.45 and min2 <= 0.45 : 
    print("Joint limits not exceeded")
    print ("test Successful")

