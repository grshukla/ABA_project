from rdkit import Chem
from rdkit.Chem import AllChem

#Finding the fingerptirint
m1 = Chem.MolFromSmiles('Cc1ccccc1')
fp1 = AllChem.GetMorganFingerprint(m1,2)


keys=fp1.GetNonzeroElements().keys()
values=fp1.GetNonzeroElements().values()

