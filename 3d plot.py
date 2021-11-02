
import matplotlib.pyplot as plt

fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection='3d')
x,y,z=([0, 1, 2, 3], [0, 22, 33, 23], [0, 23, 32, 12])


# plotting
ax.plot3D(x, y, z, 'green')

plt.show()
