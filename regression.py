from pandas import DataFrame
from sklearn import linear_model

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
f=open('/scratch/Trainee_DATA/Ramya/merged/chlavg.txt','r')
f1=open('/scratch/Trainee_DATA/Ramya/merged/pocavg.txt','r')
f2=open('/scratch/Trainee_DATA/Ramya/merged/paravg.txt','r')
x1=f1.readlines() 
x2=f2.readlines() 
y1=f.readlines()
x_1=np.loadtxt(x1)
x_2=np.loadtxt(x2)
y=np.loadtxt(y1)
x_3,x_4=np.meshgrid(x_1,x_2)
a1={'poc':x_1,'par':x_2}
df = DataFrame(a1,columns=['poc','par'])
y_i= -0.10510669487458557+x_3*0.004792 +x_4* 0.00058098
#y_i,y_2=np.meshgrid(y_i,y_i)
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(df, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
y_pred=regr.predict(df)
fig1=plt.figure()
ax = fig1.gca( projection='3d')
p=ax.scatter(x_1,x_2,y,c='g')
ax.plot_surface(x_3,x_4,y_i,rstride=1,cstride=1,linewidth=0,alpha=1)
ax.axis('equal')
ax.axis('tight') 
m_y=np.mean(y)
ss_res=sum((y-y_pred)**2)
ss_tot=sum((y-m_y)**2)
rsq=1-(float(ss_res))/ss_tot
#regr.score(df,y)