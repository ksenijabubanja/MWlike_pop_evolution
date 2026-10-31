import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import colors

# Ucitavam podatke koje sam ranije spojila
fajl = r"C:\Users\Lenovo\Desktop\Project 2025\jupyterkatalozi\interpolacija.csv"
df = pd.read_csv(fajl)



y = df['MEDIAN_M']
z=df['ZZsun']
x = df['MEDIAN_SFR']

# Polinom
def poly_surface(X, a, b, c, d, e, f):
    x, y = X
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

# Za optimizaciju parametara
popt, _ = curve_fit(poly_surface, (x, y), z)
# Izvlacenje koeficijenata
a, b, c, d, e, f = popt
x_surface, y_surface = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))
z_surface = poly_surface((x_surface, y_surface), *popt)



fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

norm = colors.Normalize(vmin=0, vmax=1.6)

# Scatter plot originalnih podataka
#ax.scatter(x, y, z, c=z, cmap='jet')

surf=ax.plot_surface(x_surface, y_surface, z_surface, cmap='jet', alpha=0.5)


ax.view_init(elev=20, azim=20)
ax.set_xlabel(r'$\log \left( \frac{\text{SFR}}{M_{\text{Sun}} \cdot \text{year}} \right)$')
ax.set_ylabel(r'$\log \left( \frac{M_{\text{stellar}}}{M_{\text{Sun}}} \right)$')
ax.set_zlabel(r'Metallicity in Sun metallicity')
ax.set_xlim([-4, 4])  # Opseg za x osu
#ax.set_xlim([min(x),max(x)])
ax.set_ylim([6, 12])  # Opseg za y osu
#ax.set_ylim([min(y),max(y)])
ax.set_zlim([0, 1.6])  # Opseg za z osu
#ax.set_zlim([min(z),max(z)])

plt.show()
