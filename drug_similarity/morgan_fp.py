from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

#Finding the Noraml fingerptirint
m1 = Chem.MolFromSmiles('Cc1ccccc1')
fp1 = AllChem.GetMorganFingerprint(m1,2)  #radius=2
keys=fp1.GetNonzeroElements().keys()
values=fp1.GetNonzeroElements().values()

#Finding fingerptints as bit vectors
fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)
n_on_bits=fp1.GetNumOnBits()          #number of on bits
on_bits=fp1.GetOnBits()               #Index of on bits

#Making a Simple Neural Net
#Making the dataset
x_data=np.zeros((len(smiles),1024))
for i in range(6):
  m1 = Chem.MolFromSmiles(smiles[i])
  fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)
  n_on_bits=fp1.GetNumOnBits() 
  on_bits=fp1.GetOnBits()
  for j in range(n_on_bits):
    x_data[i,on_bits[j]]=1
    

y_data=np.zeros((6,2))

