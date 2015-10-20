import numpy as np
import matplotlib.pyplot as plt

prop_matrix=prop_matrix[~np.all(prop_matrix == 0, axis=1)]

plt.subplot(2,3,1)
plt.hist(prop_matrix[:,0], bins=50)
plt.title('MW')
plt.subplot(2,3,2)
plt.hist(prop_matrix[:,1], bins=50)
plt.title('LogP')
plt.subplot(2,3,3)
plt.hist(prop_matrix[:,2], bins=50)
plt.title('HBD')
plt.subplot(2,3,4)
plt.hist(prop_matrix[:,3], bins=50)
plt.title('HBA')
plt.subplot(2,3,5)
plt.hist(prop_matrix[:,4], bins=50)
plt.title('PSA')
plt.subplot(2,3,6)
plt.hist(prop_matrix[:,5], bins=50)
plt.title('ROTB')
plt.show()
