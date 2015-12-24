#KDE plots 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import cPickle as pkl
import os
from matplotlib.colors import LogNorm
import seaborn as sns
import pylab

####################################
### DATA Reading ###################
####################################
f1='pyl10_apo_distance_r1.dat'
f2='pyl10_apo_distance_r2.dat'
f3='pyl10_apo_distance_r3.dat'
f4='pyl10_apo_distance_r4.dat'
f5='pyl10_apo_distance_r5.dat'

temp1=pd.read_csv(f1, sep='\s+')
x1=temp1.iloc[:,1]     #PRO92-GLY116
y1=temp1.iloc[:,2]     #HIS119-LEU121

temp2=pd.read_csv(f2, sep='\s+')
x2=temp2.iloc[:,1]     #PRO92-GLY116
y2=temp2.iloc[:,2]     #HIS119-LEU121

temp3=pd.read_csv(f3, sep='\s+')
x3=temp3.iloc[:,1]     #PRO92-GLY116
y3=temp3.iloc[:,2]     #HIS119-LEU121

temp4=pd.read_csv(f4, sep='\s+')
x4=temp4.iloc[:,1]     #PRO92-GLY116
y4=temp4.iloc[:,2]     #HIS119-LEU121

temp5=pd.read_csv(f5, sep='\s+')
x5=temp5.iloc[:,1]     #PRO92-GLY116
y5=temp5.iloc[:,2]     #HIS119-LEU121

####################################
### Plotting ### ###################
####################################

ax = sns.kdeplot(x1,y1,cmap="Blues", shade=True, shade_lowest=False)
ax.set_aspect("equal")
plt.xlim(12,25)
plt.ylim(4.5,6.5)
plt.plot(16.90,5.23,'ro',label='Apo crystal structure')
plt.plot(14.41,5.73,'yo',label='Holo crystal structure')
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/r1.png')
plt.close()


ax2 = sns.kdeplot(x2,y2,cmap="Blues", shade=True, shade_lowest=False)
ax2.set_aspect("equal")
plt.xlim(12,25)
plt.ylim(4.5,6.5)
plt.plot(16.90,5.23,'ro',label='Apo crystal structure')
plt.plot(14.41,5.73,'yo',label='Holo crystal structure')
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/r2.png')
plt.close()

ax3 = sns.kdeplot(x3,y3,cmap="Blues", shade=True, shade_lowest=False)
plt.xlim(12,25)
ax3.set_aspect("equal")
plt.ylim(4.5,6.5)
plt.plot(16.90,5.23,'ro',label='Apo crystal structure')
plt.plot(14.41,5.73,'yo',label='Holo crystal structure')
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/r3.png')
plt.close()

ax4 = sns.kdeplot(x4,y4,cmap="Blues", shade=True, shade_lowest=False)
plt.xlim(12,25)
ax4.set_aspect("equal")
plt.ylim(4.5,6.5)
plt.plot(16.90,5.23,'ro',label='Apo crystal structure')
plt.plot(14.41,5.73,'yo',label='Holo crystal structure')
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/r4.png')
plt.close()

ax5 = sns.kdeplot(x5,y5,cmap="Blues", shade=True, shade_lowest=False)
plt.xlim(12,25)
ax5.set_aspect("equal")
plt.ylim(4.5,6.5)
plt.plot(16.90,5.23,'ro',label='Apo crystal structure')
plt.plot(14.41,5.73,'yo',label='Holo crystal structure')
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/r5.png')
plt.close()
