from sympy import symbols, cos, sin, pi, simplify
from sympy.matrices import Matrix
import numpy as np
import matplotlib.pyplot as plt

rtd = 180. / np.pi  # radians to degrees
dtr = np.pi / 180.  # degrees to radians

q, alpha, d, a = symbols('theta alpha d a')


def DHP(a,d,alpha,q):

    T = Matrix([[cos(q), -sin(q), 0, a],
                   [sin(q) * cos(alpha), cos(q) * cos(alpha), -sin(alpha), -sin(alpha) * d],
                   [sin(q) * sin(alpha), cos(q) * sin(alpha), cos(alpha), cos(alpha) * d],
                   [0, 0, 0, 1]])
    return (T)


T1 = DHP(0,0,90 * dtr,q)
T2 = DHP(1,0,0* dtr,q)
T3 = DHP(1,0,0* dtr,q)

print(T1.evalf())
print(T2.evalf())
T0 = simplify(T1 * T2* T3)
print(T0.evalf())


w1 = 34 * np.pi / (5*180)
w2 = 66 * np.pi /(5*180)
strt=0
end=5
length=50
test_list = [strt + x * (end - strt)/length for x in range(length)]
for t in test_list:
    plt.clf()
    x1 = 1.2 * np.cos(w1 * t)
    y1 = 1.2 * np.sin(w1 * t)
    x2 = 1.2 * np.cos(w1 * t) + 1.6 * np.cos(w2 * t)
    y2 = 1.2 * np.sin(w1 * t) + 1.6 * np.sin(w2 * t)
    plt.plot([0, x1, x2], [0, y1, y2])
    plt.draw()
    plt.pause(0.1)


plt.show()
plt.xlim(-3, 10)
plt.ylim(-3, 10)
