import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.interpolate import SmoothBivariateSpline
from matplotlib import colors

# Ucitavam podatke koje sam ranije spojila
fajl = r"C:\Users\Lenovo\Desktop\Project 2025\jupyterkatalozi\interpolacija.csv"
df = pd.read_csv(fajl)
x = df['MEDIAN_SFR'].values
y = df['MEDIAN_M'].values
z = df['ZZsun'].values

# Grid
x_grid = np.linspace(min(x), max(x), 100)
y_grid = np.linspace(min(y), max(y), 100)
x_surface, y_surface = np.meshgrid(x_grid, y_grid)

# Spline 
spline = SmoothBivariateSpline(x, y, z, s=0.1)
z_surface = spline.ev(x_surface.ravel(), y_surface.ravel()).reshape(x_surface.shape)



fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

norm = colors.Normalize(vmin=min(z), vmax=max(z))

surf = ax.plot_surface(x_surface, y_surface, z_surface, cmap='jet', alpha=0.5)

ax.view_init(elev=20, azim=20)

ax.set_xlabel(r'$\log \left( \frac{\text{SFR}}{M_{\text{Sun}} \cdot \text{year}} \right)$')
ax.set_ylabel(r'$\log \left( \frac{M_{\text{stellar}}}{M_{\text{Sun}}} \right)$')
ax.set_zlabel(r'Metallicity in Sun metallicity')



ax.set_xlim([-4, 4])
#ax.set_xlim([min(x),max(x)])
ax.set_ylim([6, 12])  #min(y), max(y)
#ax.set_ylim([min(y),max(y)])
ax.set_zlim([0, 1.6])  
#ax.set_zlim([min(z),max(z)])

plt.show()