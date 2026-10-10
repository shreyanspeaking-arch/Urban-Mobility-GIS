import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import sys
g=gpd.read_file(input('Enter Filename'))
if 'WARD' not in list(g.columns):
    print(list(g.columns))
    m=input('Enter the column which contains the ward name/number')
    g=g.rename(columns={m:'WARD'})
if 'geometry' not in list(g.columns):
    print(list(g.columns))
    m=input('Enter the column which contains the spatial geometry of ward shapes')
    g=g.rename(columns={m:'geometry'})
g=g[['WARD','geometry']]
g=g.to_crs('EPSG:32645')
g['Perimeter (in km)']=g.length.tolist()
g['Perimeter (in km)']*=(10**(-3))
f=input('Enter filename in which you would like to see the list of wards along with their perimeters. Exclude .xlsx')
g[['WARD','Perimeter (in km)']].to_excel(f+'.xlsx',index=False)
g=g.to_crs('EPSG:4326')

fig,ax=plt.subplots(figsize=(6,6))
g.plot(ax=ax,column='Perimeter (in km)',cmap='YlGnBu',legend=True,edgecolor='Black',linewidth=1)
ax.set_title('Map Displaying the size of wards by perimeter in km')
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()
plt.show()
