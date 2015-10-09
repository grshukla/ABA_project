
# coding: utf-8

# In[1]:

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import cPickle as pkl
import os
from matplotlib.colors import LogNorm


# In[2]:
####### We have four files containing 3 columns each#########
####### Each column represents a distance metric#############
####### We plot the contour plots in this script#############
f1='pyl2_apo_distance.dat'
f2='pyl2_holo_distance.dat'
f3='pyl10_apo_distance.dat'
f4='pyl10_holo_distance.dat'


# In[3]:

temp=pd.read_csv(f1, sep='\s+')
dataset1=temp.iloc[:,1]
dataset2=temp.iloc[:,2]
dataset3=temp.iloc[:,3]
x1=np.array(dataset1)
y1=np.array(dataset2)
z1=np.array(dataset3)


# In[4]:

temp=pd.read_csv(f2, sep='\s+')
dataset1=temp.iloc[:,1]
dataset2=temp.iloc[:,2]
dataset3=temp.iloc[:,3]
x2=np.array(dataset1)
y2=np.array(dataset2)
z2=np.array(dataset3)


# In[5]:

temp=pd.read_csv(f3, sep='\s+')
dataset1=temp.iloc[:,1]
dataset2=temp.iloc[:,2]
dataset3=temp.iloc[:,3]
x3=np.array(dataset1)
y3=np.array(dataset2)
z3=np.array(dataset3)


# In[6]:

temp=pd.read_csv(f4, sep='\s+')
dataset1=temp.iloc[:,1]
dataset2=temp.iloc[:,2]
dataset3=temp.iloc[:,3]
x4=np.array(dataset1)
y4=np.array(dataset2)
z4=np.array(dataset3)


# In[7]:

plt.subplot(2,1,1)
plt.hist2d(y3,x3, bins=500, norm=LogNorm())
cb=plt.colorbar()
cb.set_label("Number of structures in bin",fontsize=20)
plt.title("Confomational landscape of PYL10 apo structure",fontsize=20)
plt.xlabel('Distance: PRO (nm)',fontsize=20)
plt.ylabel('Distance HIS (ns)',fontsize=20)

#plt.scatter(0,13, marker='<', color='r')
#plt.scatter(2,0,marker='<', color='r')

plt.subplot(2,1,2)
plt.hist2d(y4,x4, bins=500, norm=LogNorm())
cb=plt.colorbar()
cb.set_label("Number of structures in bin",fontsize=20)
plt.title("Confomational landscape of PYL10 holo structure",fontsize=20)
plt.xlabel('Distance: PRO (nm)',fontsize=20)
plt.ylabel('Distance HIS (ns)',fontsize=20)


plt.show()


# In[38]:

plt.subplot(2,1,1)
plt.hist2d(y1,x1, bins=200, norm=LogNorm())
cb=plt.colorbar()
cb.set_label("Number of structures in bin",fontsize=20)
#plt.title("Confomational landscape of PYL10 apo structure",fontsize=20)
#plt.xlabel('Distance: PRO (nm)',fontsize=20)
plt.ylabel('Distance HIS (ns)',fontsize=20)
plt.xlim(4.5,6.5)
plt.ylim(10,22)

#plt.scatter(0,13, marker='<', color='r')
#plt.scatter(2,0,marker='<', color='r')

plt.subplot(2,1,2)
plt.hist2d(y2,x2, bins=200, norm=LogNorm())
cb=plt.colorbar()
cb.set_label("Number of structures in bin",fontsize=20)
#plt.title("Confomational landscape of PYL10 holo structure",fontsize=20)
plt.xlabel('Distance: PRO (nm)',fontsize=20)
plt.ylabel('Distance HIS (ns)',fontsize=20)
plt.xlim(4.5,6.5)
plt.ylim(10,22)


plt.show()


# In[25]:

hist2=plt.hist2d(y2,x2, bins=200)


# In[42]:

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]


# In[43]:

plt.contourf(X,Y,Z)
plt.colorbar()


# In[44]:

plt.show()


# In[93]:

#Comparison of apo and holo PYL2
plt.subplot(2,1,1)
hist2=plt.hist2d(x1,y1, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS119-LEU121($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL2 Apo')

plt.subplot(2,1,2)
hist2=plt.hist2d(x2,y2, bins=200)

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel(' Distance: PRO92-GLY116($\AA$)',fontsize=15)
plt.ylabel(' Distance: HIS119-LEU121($\AA$)',fontsize=15)
plt.text(18, 6.2, 'PYL2 Holo')
plt.show()


# In[94]:

#Comparison of apo and holo PYL10
plt.subplot(2,1,1)
hist2=plt.hist2d(x3,y3, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS111-LEU113  ($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL10 Apo')

plt.subplot(2,1,2)
hist2=plt.hist2d(x4,y4, bins=200)

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel('Distance: PRO84-GLY108  ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL10 Holo')
plt.show()


# In[102]:

#Comparison of ABA binding PYL2 APO vs PYL10 Apo
plt.subplot(2,1,1)
hist2=plt.hist2d(x1,z1, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,20)
plt.ylim(20,55)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.ylabel('Distance ABA-LYS64 ($\AA$)',fontsize=15)
plt.text(19,50, 'PYL2 Apo')

plt.subplot(2,1,2)
hist2=plt.hist2d(x3,z3, bins=200)

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,20)
plt.ylim(20,55)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel('Distance: PRO84-GLY108($\AA$)',fontsize=15)
plt.ylabel(' Distance ABA-LYS64 ($\AA$)',fontsize=15)
plt.text(19,50, 'PYL10 Apo')
plt.show()


# In[108]:

#Comparison of ABA binding 
plt.subplot(2,1,1)
hist2=plt.hist2d(x1,z1, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19.5)
plt.ylim(20,55)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.ylabel('Distance ABA-LYS64 ($\AA$)',fontsize=15)
plt.text(19,50, 'PYL2 Apo')

plt.subplot(2,1,2)
hist2=plt.hist2d(x2,z2, bins=200)

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19.5)
#plt.ylim(20,55)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel('Distance: PRO84-GLY108($\AA$)',fontsize=15)
plt.ylabel(' Distance ABA-LYS64 ($\AA$)',fontsize=15)
plt.text(19,9, 'PYL2 Holo')
plt.show()


# In[110]:

#Comparison of PYL2 and PYL10 apo
plt.subplot(2,1,1)
hist2=plt.hist2d(x1,y1, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS119-LEU121($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL2 Apo')

plt.subplot(2,1,2)
hist2=plt.hist2d(x3,y3, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel('Distance: PRO84-GLY108   ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS111-LEU113  ($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL10 Apo')
plt.show()


# In[113]:

plt.subplot(2,1,1)
hist2=plt.hist2d(x2,y2, bins=200)

Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
#plt.xlabel(' Distance: PRO92-GLY116($\AA$)',fontsize=15)
plt.ylabel(' Distance: HIS119-LEU121($\AA$)',fontsize=15)
plt.text(18, 6.2, 'PYL2 Holo')


plt.subplot(2,1,2)
hist2=plt.hist2d(x4,y4, bins=200)
Z=hist2[0]
Z=Z/np.sum(Z)
X=hist2[1][0:200]
Y=hist2[2][0:200]
plt.contourf(X,Y,Z)
plt.xlim(12.5,19)
plt.ylim(5,6.5)
cb=plt.colorbar()
cb.set_label("Fractional structure population",fontsize=15)
plt.xlabel('Distance: PRO84-GLY108  ($\AA$)',fontsize=15)
plt.ylabel('Distance: HIS111-LEU113 ($\AA$)',fontsize=15)
plt.text(18,6.2, 'PYL10 Holo')
plt.show()


# In[ ]:



