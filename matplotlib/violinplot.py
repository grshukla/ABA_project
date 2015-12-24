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
y1=temp1.iloc[:,3]     

temp2=pd.read_csv(f2, sep='\s+')
x2=temp2.iloc[:,1]     #PRO92-GLY116
y2=temp2.iloc[:,3]     #HIS119-LEU121

temp3=pd.read_csv(f3, sep='\s+')
x3=temp3.iloc[:,1]     #PRO92-GLY116
y3=temp3.iloc[:,3]     #HIS119-LEU121

temp4=pd.read_csv(f4, sep='\s+')
x4=temp4.iloc[:,1]     #PRO92-GLY116
y4=temp4.iloc[:,3]     #HIS119-LEU121

temp5=pd.read_csv(f5, sep='\s+')
x5=temp5.iloc[:,1]     #PRO92-GLY116
y5=temp5.iloc[:,3]     #HIS119-LEU121

e=[]
e.append(y1)
e.append(y2)
e.append(y3)
e.append(y4)
e.append(y5)

sns.violinplot(data=e, palette="Set3", bw=.2, cut=1, linewidth=1)
plt.savefig('/Users/Saurabh/Dropbox/My_Papers_and_Reports/Lab_Meeting_Presentations/20Dec2015/images/aba_violin.png')
