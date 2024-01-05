import numpy as np
import numpy.ma as ma
import h5py as h5
import matplotlib.pyplot as plt
from os import path
import glob
import netCDF4 as nc
#from eofs.standard import Eof
ip ='/scratch/Trainee_DATA/Muhilan/project_2019/data/NOAA_DATASET/olr_anomaly/2001_olr_daily_anom.h5'


f1 =h5.File (ip,'r')
olr =f1['/anom'] [0:181,30:43,:]
lat =f1['/lat'] [30:43]
lon =f1['/lon'] [:]

hov = np.zeros((181,144))



for i in range (181):
    olr1 = olr[i,:,:]
    olr2 = np.mean(olr1,axis=0)
    hov[i,:] = olr2
    
hov2 = np.flipud(hov)

y = np.flipud(np.arange(0,181,15))
cs = plt.contourf(hov2,levels=[-110,-90,-70,-50,-30,-10,10,30,50,70,90],colors = ['k','navy','indigo','mediumpurple','slateblue','white','sandybrown','peru','chocolate','maroon'])
plt.xticks((np.arange(0,144+24,24)),('0','60E','120E','180','120W','60W','0'),fontsize = 10)#weight = 'bold')
plt.yticks((y),('1 Jan 2001','16 Jan 2001','31 Jan 2001','15 Feb 2001','2 Mar 2001','17 Mar 2001','1 Apr 2001','16 Apr 2001','1 May 2001','16 May 2001','31 May 2001','15 Jun 2001','30 Jun 2001'),fontsize = 10)#,weight = 'bold')
plt.colorbar(cs) 
plt.xlabel('Longitude')
plt.text(50,184,'OLR Anomalies : W/m${^2}$',fontsize = 15)
plt.text(0,182,'1 Jan 2001 : 30 Jun 2001',fontsize = 15,weight = 'bold')
plt.text(120,182,'-15S-15N',fontsize = 15,weight = 'bold')