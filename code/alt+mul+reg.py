import numpy as np
import scipy.linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
f=open('/scratch/Trainee_DATA/Ramya/merged/plots/Nitrate/2014/Annual/mean/2014.txt','r')
f1=open('/scratch/Trainee_DATA/Ramya/merged/chlavg.txt','r')
f2=open('/scratch/Trainee_DATA/Ramya/merged/sstavg.txt','r')
x=np.loadtxt(f1)
y=np.loadtxt(f2)
z=np.loadtxt(f)
data = np.c_[x,y,z]
mn = np.min(data, axis=0)
mx = np.max(data, axis=0)
x1,y1 = np.meshgrid(np.linspace(mn[0], mx[0], 60), np.linspace(mn[1], mx[1], 60))
# regular grid covering the domain of the data
#x1,y1 = np.meshgrid(x,y)
a = np.c_[data[:,0], data[:,1], np.ones(data.shape[0])]
c,_,_,_ = scipy.linalg.lstsq(a, data[:,2])
z_r=c[0]*x + c[1]*y + c[2]
z1= c[0]*x1 + c[1]*y1 + c[2]
#m_z=np.mean(z)
fig1 = plt.figure(figsize=(10, 10))
ax = plt.gca(projection='3d')
ax.plot_wireframe(x1,y1,z1, rstride=4, cstride=4, alpha=0.3)
ax.scatter(data[:,0], data[:,1], data[:,2], c='r', s=50)
plt.xlabel('Chlorophyll')
plt.ylabel('SST')
ax.set_zlabel('Nitrate')
ax.axis('equal')
ax.axis('tight')
m_z=np.mean(z)
ss_res=sum((z-z_r)**2)
ss_tot=sum((z-m_z)**2)
rsq=1-(float(ss_res))/ss_tot
ax.text(1,31,2.9,"R$^2$=0.242",fontsize=14)
ax.text(1,31,2.8,"N=60",fontsize=14)
plt.title("Nitrate_Linear fit",fontsize=20,fontweight="bold")
np.sqrt(rsq)