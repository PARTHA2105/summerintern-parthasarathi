import numpy as np
from netCDF4 import Dataset as nc
import matplotlib.pyplot as plt
import numpy.ma as ma
from mpl_toolkits.basemap import Basemap,cm

f=nc('/scratch/Trainee_DATA/Ramya/DATA/363163975/L3m_20140101-20140131__363163975_4_AV-MOD_CHL1_MO_00.nc','r')
print f.variables
lat=f.variables['lat'][:]
lon=f.variables['lon'][:]
chl=f.variables['CHL1_mean'][:]


chl1=ma.masked_where(chl>2.0,chl)
lon1,lat1 = np.meshgrid(lon,lat)
f.close()

f1=nc('/scratch/Trainee_DATA/Ramya/sst_data/A20140012014031.L3m_MO_SST_sst_4km.nc','r')
print f1.variables
lat_s=f1.variables['lat'][:]
lon_s=f1.variables['lon'][:]
sst=f1.variables['sst'][:]


sst1=ma.masked_where(sst<20,sst)
sst2=ma.masked_where(sst1>35,sst1)

lon1_s,lat1_s = np.meshgrid(lon_s,lat_s)
f.close()
fig=plt.figure(figsize=(10,10))
n=Basemap
m = Basemap(projection = 'cyl',llcrnrlat=5.0,llcrnrlon=75.0,urcrnrlat=25.0,urcrnrlon=95.0,resolution='l')
m.drawparallels(np.arange(-90, 90,5.0),labels=[1,0,0,0], color = 'g',dashes=[4, 2], linewidth = 0.40)
m.drawmeridians(np.arange(-180,180,5.0),labels=[0,0,0,1], color = 'g', dashes=[4, 2], linewidth = 0.40)
m.drawcoastlines(linewidth=0.5)
m.drawmapboundary(fill_color='white')
##m.fillcontinents(color='white',lake_color='white')
cp = plt.contour(lon1_s, lat1_s, sst2)
plt.colorbar(cp)
#plt.title('Filled Contours Plot')
#plt.xlabel('x (cm)')
#plt.ylabel('y (cm)')
#plt.show()                    


im=m.pcolormesh(lon1,lat1,chl1,cmap=plt.cm.jet,latlon=True)
m.colorbar(im, location='bottom', pad='7%',label="deg C")

plt.xlabel('Longitude', labelpad=20)
plt.ylabel('Latitude', labelpad=40)
plt.title('Chlorophyll concentration with SST Data_jan 2014')
plt.show() 
plt.savefig('/scratch/Trainee_DATA/Ramya/monthly/chl and SST_Jan_2014.png')