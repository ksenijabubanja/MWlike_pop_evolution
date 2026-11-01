import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv(r'C:\Users\Lenovo\Desktop\Project 2025\jupyterkatalozi\katalog.csv')


#binovi za masu i SFR (stavila sam npr po 20 binova)
sfr_bins = pd.cut(data['MEDIAN_SFR'], bins=2000)
mass_bins = pd.cut(data['MEDIAN_M'], bins=2000)  

# Dodajem kolone za binove u DataFrame
data['sfr_bin'] = sfr_bins
data['mass_bin'] = mass_bins


# Grupisem po binovima i izracunam medijanu metalicnosti za svaku grupu
median_metallicity = data.groupby(['sfr_bin','mass_bin'])['MEDIAN_Zg'].median().reset_index()

# izracunam srednju vrednost za svaki bin
# 'mid' za sredinu svakog bina

median_metallicity['sfr_bin_center'] = median_metallicity['sfr_bin'].apply(lambda x: x.mid)
median_metallicity['mass_bin_center'] = median_metallicity['mass_bin'].apply(lambda x: x.mid)




fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')




sc = ax.scatter(median_metallicity['sfr_bin_center'], 
                median_metallicity['mass_bin_center'], 
                median_metallicity['MEDIAN_Zg'], 
                c=median_metallicity['MEDIAN_Zg'], cmap='jet', s=10)



#ovde sam stavila random vrednosti kao placeholder
#x.scatter(2, 10.6, 7, s=100, marker='o', color='black')




ax.set_ylabel('Mass (log(M/M☉))')
ax.set_xlabel('SFR (log(M/yr))')
ax.set_zlabel('Metallicity')


fig.colorbar(sc, label='Metallicity')



plt.show()
