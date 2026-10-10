import geopandas as gpd
import osmnx as ox
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
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

G=ox.graph_from_polygon(g.union_all(),network_type='drive')
G=ox.convert.to_undirected(G)
nodes,edges=ox.graph_to_gdfs(G)
edges=edges.to_crs(g.estimate_utm_crs())
g=g.to_crs(g.estimate_utm_crs())
r=gpd.overlay(edges,g,how='intersection')
r['length'] = r.length
r=r[['WARD','length']]
g['Area']=list(g.area)
g['Area']*=10**(-6)
r['length']*=10**(-3)
r=r.groupby(['WARD'])['length'].agg('sum')
g=g.set_index('WARD')
r=pd.merge(r,g,how='right',left_index=True,right_index=True)
r=r.rename(columns={'Area':'Area of Ward(in sqkm)','length':'Approximate Total Length of roads in ward(in km)'})
r['Road Density (km/km2)']=r['Approximate Total Length of roads in ward(in km)']/r['Area of Ward(in sqkm)']
r=r.sort_index()
r=r.reset_index()
r=gpd.GeoDataFrame(r,geometry='geometry',crs=g.crs)
f=input('Enter Output Filename. Exclude .xlsx')
r.to_excel(f+'.xlsx',index=False)
r=r.to_crs('EPSG:4326')
fig,ax=plt.subplots(figsize=(6,6))
r.plot(ax=ax,column='Road Density (km/km2)',cmap='YlGnBu',legend=True,edgecolor='Black',linewidth=1)
ax.set_title('Map Displaying the road density of wards (km/km2)')
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()
plt.show()
