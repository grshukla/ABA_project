from rdkit import Chem
from rdkit.Chem import AllChem

#Finding the Noraml fingerptirint
m1 = Chem.MolFromSmiles('Cc1ccccc1')
fp1 = AllChem.GetMorganFingerprint(m1,2)  #radius=2
keys=fp1.GetNonzeroElements().keys()
values=fp1.GetNonzeroElements().values()

#Finding fingerptints as bit vectors
fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)
n_on_bits=fp1.GetNumOnBits()          #number of on bits
on_bits=fp1.GetOnBits()               #Index of on bits



