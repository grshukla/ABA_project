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

plt.subplot(2,3,2)
sns.distplot(prop_matrix[:,1], color="lightskyblue",bins=500, kde=True, kde_kws={"color": "k"})
plt.xlim(-8,10)

plt.subplot(2,3,3)
sns.distplot(prop_matrix[:,2], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k"})
plt.xlim(0,12)

plt.subplot(2,3,4)
sns.distplot(prop_matrix[:,3], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k"})
plt.xlim(0,18)

plt.subplot(2,3,5)
sns.distplot(prop_matrix[:,4], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k"})
plt.xlim(0,300)

plt.subplot(2,3,6)
sns.distplot(prop_matrix[:,5], color="lightskyblue",bins=20, kde=True, kde_kws={"color": "k"})
plt.xlim(0,25)

plt.show()


