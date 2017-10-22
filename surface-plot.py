from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy import misc

face = misc.imread("pnoise2.png")[:, :, 1]

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, face.shape[0])
Y = np.arange(0, face.shape[1])
X, Y = np.meshgrid(X, Y)
Z = face[X, Y]

colormap = cm.plasma


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=colormap, linewidth=0, antialiased=True)

# remove stuff
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


plt.show()
