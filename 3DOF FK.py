from sympy import symbols, cos, sin, pi, simplify
#from sympy.matrices import Matrix
import numpy as np
import matplotlib.pyplot as plt
rtd = 180. / np.pi  # radians to degrees
dtr = np.pi / 180.  # degrees to radians



def DHP(a,d,alpha,q):

    T = np.array([[cos(q), -sin(q) * cos(alpha), sin(q) * sin(alpha), a * cos(q)],
                  [sin(q), cos(q) * cos(alpha), -cos(q) * sin(alpha), a * sin(q)],
                  [0, sin(alpha), cos(alpha), d],
                  [0, 0, 0, 1]])

    return (T)
#Alldeclarations
T=5
thetainit1=0
thetainit2=0
thetainit3=0

theta1 =float(input('enter theta1 :')) * dtr
theta2 =float(input('enter theta2 :')) * dtr
theta3 =float(input('enter theta3 :')) * dtr

w1=(theta1-0)/T
w2=(theta2-0)/T
w3=(theta3-0)/T



plt.style.use('ggplot')
fig = plt.figure()
i=0
while i<=1 :
    plt.clf()
#calling the DH parameter function
    theta1= thetainit1 + (w1 * i* T)
    theta2 =thetainit2 + (w2 * i * T)
    theta3 =thetainit3 + (w3 * i * T)
    i=i+0.01

    T1 = DHP(0, 0, 90 * dtr, theta1)
    T2 = DHP(1, 0, 0 * dtr, theta2)
    T3 = DHP(1, 0, 0 * dtr, theta3)

#assigning coordinate values from matrix
    TA =T1
    TB =np.dot(T1,T2)
    TC =np.dot(TB,T3)
    x1 =TA[0,3]
    x2 =TB[0,3]
    x3 =TC[0,3]
    y1 =TA[1,3]
    y2 =TB[1,3]
    y3 =TC[1,3]
    z1 =TA[2,3]
    z2 =TB[2,3]
    z3 =TC[2,3]
    print(x3,y3,z3)
#Ploting on axes3d
    ax = plt.axes(projection='3d')
    ax.plot3D([0, x1, x2, x3], [0, y1, y2, y3], [0, z1, z2, z3])
    ax.scatter([0, x1, x2, x3], [0, y1, y2, y3], [0, z1, z2, z3])
    ax.text(x3, y3, z3,[x3,y3,z3])
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(-2, 2)
    plt.pause(T*0.01)

plt.pause(10)




