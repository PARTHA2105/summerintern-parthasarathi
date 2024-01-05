import numpy as np
import numpy.ma as ma
from netCDF4 import Dataset as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

f=nc('/scratch/Trainee_DATA/Ramya/DATA/363163975/L3m_20140101-20140131__363163975_4_AV-MOD_CHL1_MO_00.nc','r')
print f.variables
lat=f.variables['lat'][:]
lon=f.variables['lon'][:]
chl=f.variables['CHL1_mean'][:]



latselect = np.logical_and(lat>=8.,lat<=13.5)
lonselect = np.logical_and(lon>=77.5,lon<=95.)
lat_s2 = f.variables['lat'][latselect]
lon_s2 =f.variables['lon'][lonselect]
chl= f.variables['CHL1_mean'][latselect,lonselect]



chl1=ma.masked_where(chl>2.01,chl)
lon1,lat1 = np.meshgrid(lon_s2,lat_s2)
f.close()
fig=plt.figure(figsize=(10,10))
n=Basemap
m = Basemap(projection = 'cyl',llcrnrlat=5.0,llcrnrlon=77.5,urcrnrlat=23.0,urcrnrlon=95.0,resolution='l')
m.drawparallels(np.arange(-90, 90,5.0),labels=[1,0,0,0], color = 'g',dashes=[4, 2], linewidth = 0.40)
m.drawmeridians(np.arange(-180,180,5.0),labels=[0,0,0,1], color = 'g', dashes=[4, 2], linewidth = 0.40)
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary(fill_color='white')
#m.fillcontinents(color='white',lake_color='white')



im=m.pcolormesh(lon1,lat1,chl1,cmap=plt.cm.jet,latlon=True)
m.colorbar(im, location='right', pad='5%',label="mg/m3")

plt.xlabel('Longitude', labelpad=20)
plt.ylabel('Latitude', labelpad=40)
plt.title('Chlorophyll_Odisha_(Jan)2014')
plt.show() 
plt.savefig('/scratch/Trainee_DATA/Ramya/DATA/sample_code/CHL_Odisha_(jan)2014.png')