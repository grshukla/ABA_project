import seaborn as sns
import numpy as np
import cPickle as pkl
from matplotlib import pyplot as plt

g= open('prop_matrix.pkl', 'rb')
prop_matrix=pkl.load(g)
g.close()

MW=prop_matrix[:,0]

plt.subplot(2,3,1)
sns.distplot(MW, color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k"})
plt.xlim(0,1000)
plt.xlabel('MW',fontsize=20)
plt.ylabel('Density',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,2)
sns.distplot(prop_matrix[:,1], color="lightskyblue",bins=300, kde=True, kde_kws={"color": "k","bw": "0.1"})
plt.xlim(-8,10)
plt.xlabel('Log(P)',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,3)
sns.distplot(prop_matrix[:,2], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k", "bw": "0.4"})
plt.xlim(0,12)
plt.xlabel('HBD',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,4)
sns.distplot(prop_matrix[:,3], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k", "bw":"0.5"})
plt.xlim(0,18)
plt.xlabel('HBA',fontsize=20)
plt.ylabel('Density',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,5)
sns.distplot(prop_matrix[:,4], color="lightskyblue",bins=30, kde=True, kde_kws={"color": "k"})
plt.xlim(0,300)
plt.xlabel('ROTB',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,6)
sns.distplot(prop_matrix[:,5], color="lightskyblue",bins=70, kde=True, kde_kws={"color": "k"})
plt.xlim(0,25)
plt.xlabel('PSA',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.show()

######################NEW PROPS#######################
plt.subplot(2,3,1)
sns.distplot(smiles_matrix[:,0], color="lightskyblue",bins=10, kde=True, kde_kws={"color": "k", "bw" : "0.5"})
plt.xlim(0,5)
plt.xlabel('# of Arom rings',fontsize=20)
plt.ylabel('Density',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)


plt.subplot(2,3,2)
sns.distplot(smiles_matrix[:,6], color="lightskyblue",bins=10, kde=True, kde_kws={"color": "k","bw": "0.5"})
plt.xlim(0,10)
plt.xlabel('# of Rings',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)


plt.subplot(2,3,3)
sns.distplot(smiles_matrix[:,2], color="lightskyblue",bins=30, kde=True, kde_kws={"color": "k", "bw": "1"})
plt.xlim(0,40)
plt.xlabel('# of Heavy Atoms',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,4)
sns.distplot(smiles_matrix[:,4], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k", "bw":"1"})
plt.xlim(0,30)
plt.xlabel('# of HeteroAtoms',fontsize=20)
plt.ylabel('Density',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,5)
sns.distplot(smiles_matrix[:,5], color="lightskyblue",bins=50, kde=True, kde_kws={"color": "k"})
plt.xlim(0,200)
plt.xlabel('# of valence e',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.subplot(2,3,6)
sns.distplot(smiles_matrix[:,7], color="lightskyblue",bins=10, kde=True, kde_kws={"color": "k"})
plt.xlim(0,1)
plt.xlabel('Fraction of sp3 C',fontsize=20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.show()
