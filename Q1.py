import numpy as np
import matplotlib.pyplot as plt

#Arm Function
def Armconfig(L1,L2,theta1,theta2) :
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)
    x2 = L1*np.cos(theta1) + L2*np.cos(theta1+theta2)
    y2 = L1*np.sin(theta1) + L2*np.sin(theta1+theta2)
    return(x1,y1,x2,y2)



L1=float(input('Enter L1 :'))
L2=float(input('Enter L2 :'))
theta1=float(input('Enter theta1 in degree:'))*np.pi/180
theta2=float(input('Enter theta2 in degree:'))*np.pi/180

x1,y1,x2,y2=Armconfig(L1,L2,theta1,theta2)


print("Joint 1 at x =", x1, "y =",y1)
print("End Effector at x =",x2, "y =",y2)

plt.plot([0,x1,x2],[0,y1,y2])
plt.show()