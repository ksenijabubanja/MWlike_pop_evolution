import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
fajl = r"C:\Users\Lenovo\Desktop\Project 2025\jupyterkatalozi\katalog.csv"
df = pd.read_csv(fajl)
y = df['MEDIAN_M']
x = df['MEDIAN_SFR']
z = df['MEDIAN_Zg']

# Poli fit
def poly_surface(X, a, b, c, d, e, f):
    x, y = X
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

popt, _ = curve_fit(poly_surface, (x, y), z)

#ovde sam stavila 50x50 za testni prikaz
x_lin = np.linspace(min(x), max(x), 50)
y_lin = np.linspace(min(y), max(y), 50)
X_mesh, Y_mesh = np.meshgrid(x_lin, y_lin)
# Racunanje Zg za svaku kombinaciju
Zg_mesh = poly_surface((X_mesh, Y_mesh), *popt)

ZZsun_mesh = 10 ** (Zg_mesh - 8.69)





X_flat = X_mesh.ravel()
Y_flat = Y_mesh.ravel()
ZZsun_flat = ZZsun_mesh.ravel()

# DataFrame
interpolacija = pd.DataFrame({
    'MEDIAN_SFR': X_flat,
    'MEDIAN_M': Y_flat,
    'ZZsun': ZZsun_flat
})

interpolacija.index = range(len(interpolacija))
interpolacija.to_csv(r"C:\Users\Lenovo\Desktop\Project 2025\jupyterkatalozi\interpolacija.csv", index=False)

print(interpolacija.head())
