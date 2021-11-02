import numpy as np
import matplotlib.pyplot as plt



def Print():
    plt.style.use('ggplot')
    Q1 = np.linspace(0, np.radians(22), 100)
    Q2 = np.linspace(0, np.radians(34), 100)
    Q3 = np.linspace(0, np.radians(45), 100)

    L1 = 1.2
    L2 = 1.6
    L3 = 1.8



    for i in range(1, 100, 1):
        plt.clf()
        q1 = Q1[i]
        q2 = Q2[i]
        q3 = Q3[i]
        x1 = L1 * np.cos(q1)
        y1 = L1 * np.sin(q1)
        x2 = L1 * np.cos(q1) + L2 * np.cos(q1 + q2)
        y2 = L1 * np.sin(q1) + L2 * np.sin(q1 + q2)
        x3 = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) +  L3 * np.cos(q1 + q2+ q3)
        y3 = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) +  L3 * np.sin(q1 + q2 + q3)

        plt.plot([0, x1, x2,x3], [0, y1, y2,y3] )
        plt.draw()
        plt.legend(fontsize=15)
        plt.plot(0, 0, 'ro', markersize=5, label='origin')
        plt.plot(x1, y1, 'ro', markersize=5, label='joint1')
        plt.plot(x2, y2, 'ro', markersize=5, label='end effector')
        plt.plot(x3, y3, 'ro', markersize=5, label='end effector')
        plt.xlim(-1, 6)
        plt.ylim(-1, 6)
        plt.pause(0.05)

    plt.pause(10)
    return(0)
Print()




