#Takes the Smiles string as input and produces the feature vectors

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import Fragments
from rdkit.Chem import GraphDescriptors

######################################################################
# Function for physicochemical featurization matrix of a smile string#
######################################################################


def phys_featurizer(s):
  m=Chem.MolFromSmiles(s)
  phys_features=[]
  #Featurization begins
  phys_features.append(Descriptors.BertzCT(m))
  phys_features.append(Descriptors.Chi0(m))
  phys_features.append(Descriptors.Chi0n(m))
  phys_features.append(Descriptors.Chi0v(m))
  phys_features.append(Descriptors.Chi1(m))
  phys_features.append(Descriptors.Chi1n(m))
  phys_features.append(Descriptors.Chi1v(m))
  phys_features.append(Descriptors.Chi2n(m))
  phys_features.append(Descriptors.Chi2v(m))
  phys_features.append(Descriptors.Chi3n(m))
  phys_features.append(Descriptors.Chi3v(m))
  phys_features.append(Descriptors.Chi4n(m))
  phys_features.append(Descriptors.Chi4v(m))
  phys_features.append(Descriptors.EState_VSA1(m))
  phys_features.append(Descriptors.EState_VSA10(m))
  phys_features.append(Descriptors.EState_VSA11(m))
  phys_features.append(Descriptors.EState_VSA2(m))
  phys_features.append(Descriptors.EState_VSA3(m))
  phys_features.append(Descriptors.EState_VSA4(m))
  phys_features.append(Descriptors.EState_VSA5(m))
  phys_features.append(Descriptors.EState_VSA6(m))
  phys_features.append(Descriptors.EState_VSA7(m))
  phys_features.append(Descriptors.EState_VSA8(m))
  phys_features.append(Descriptors.EState_VSA9(m))
  phys_features.append(Descriptors.ExactMolWt(m))
  phys_features.append(Descriptors.FractionCSP3(m))
  phys_features.append(Descriptors.HallKierAlpha(m))
  phys_features.append(Descriptors.HeavyAtomCount(m))
  phys_features.append(Descriptors.HeavyAtomMolWt(m))
  phys_features.append(Descriptors.Ipc(m))
  phys_features.append(Descriptors.Kappa1(m))
  phys_features.append(Descriptors.Kappa2(m))
  phys_features.append(Descriptors.Kappa3(m))
  phys_features.append(Descriptors.LabuteASA(m))
  phys_features.append(Descriptors.MaxAbsEStateIndex(m))
  phys_features.append(Descriptors.MaxAbsPartialCharge(m))
  phys_features.append(Descriptors.MaxEStateIndex(m))
  phys_features.append(Descriptors.MaxPartialCharge(m))
  phys_features.append(Descriptors.MinAbsEStateIndex(m))
  phys_features.append(Descriptors.MinAbsPartialCharge(m))
  phys_features.append(Descriptors.MinEStateIndex(m))
  phys_features.append(Descriptors.MinPartialCharge(m))
  phys_features.append(Descriptors.MolLogP(m))
  phys_features.append(Descriptors.MolMR(m))
  phys_features.append(Descriptors.MolWt(m))
  phys_features.append(Descriptors.NHOHCount(m))
  phys_features.append(Descriptors.NOCount(m))
  phys_features.append(Descriptors.NumAliphaticCarbocycles(m))
  phys_features.append(Descriptors.NumAliphaticHeterocycles(m))
  phys_features.append(Descriptors.NumAliphaticRings(m))
  phys_features.append(Descriptors.NumAromaticCarbocycles(m))
  phys_features.append(Descriptors.NumAromaticHeterocycles(m))
  phys_features.append(Descriptors.NumAromaticRings(m))
  phys_features.append(Descriptors.NumHAcceptors(m))
  phys_features.append(Descriptors.NumHDonors(m))
  phys_features.append(Descriptors.NumHeteroatoms(m))
  phys_features.append(Descriptors.NumRadicalElectrons(m))
  phys_features.append(Descriptors.NumRotatableBonds(m))
  phys_features.append(Descriptors.NumSaturatedCarbocycles(m))
  phys_features.append(Descriptors.NumSaturatedHeterocycles(m))
  phys_features.append(Descriptors.NumSaturatedRings(m))
  phys_features.append(Descriptors.NumValenceElectrons(m))
  phys_features.append(Descriptors.PEOE_VSA1(m))
  phys_features.append(Descriptors.PEOE_VSA10(m))
  phys_features.append(Descriptors.PEOE_VSA11(m))
  phys_features.append(Descriptors.PEOE_VSA12(m))
  phys_features.append(Descriptors.PEOE_VSA13(m))
  phys_features.append(Descriptors.PEOE_VSA14(m))
  phys_features.append(Descriptors.PEOE_VSA2(m))
  phys_features.append(Descriptors.PEOE_VSA3(m))
  phys_features.append(Descriptors.PEOE_VSA4(m))
  phys_features.append(Descriptors.PEOE_VSA5(m))
  phys_features.append(Descriptors.PEOE_VSA6(m))
  phys_features.append(Descriptors.PEOE_VSA7(m))
  phys_features.append(Descriptors.PEOE_VSA8(m))
  phys_features.append(Descriptors.PEOE_VSA9(m))
  phys_features.append(Descriptors.RingCount(m))
  phys_features.append(Descriptors.SMR_VSA1(m))
  phys_features.append(Descriptors.SMR_VSA10(m))
  phys_features.append(Descriptors.SMR_VSA2(m))
  phys_features.append(Descriptors.SMR_VSA3(m))
  phys_features.append(Descriptors.SMR_VSA4(m))
  phys_features.append(Descriptors.SMR_VSA5(m))
  phys_features.append(Descriptors.SMR_VSA6(m))
  phys_features.append(Descriptors.SMR_VSA7(m))
  phys_features.append(Descriptors.SMR_VSA8(m))
  phys_features.append(Descriptors.SMR_VSA9(m))
  phys_features.append(Descriptors.SlogP_VSA1(m))
  phys_features.append(Descriptors.SlogP_VSA10(m))
  phys_features.append(Descriptors.SlogP_VSA11(m))
  phys_features.append(Descriptors.SlogP_VSA12(m))
  phys_features.append(Descriptors.SlogP_VSA2(m))
  phys_features.append(Descriptors.SlogP_VSA3(m))
  phys_features.append(Descriptors.SlogP_VSA4(m))
  phys_features.append(Descriptors.SlogP_VSA5(m))
  phys_features.append(Descriptors.SlogP_VSA6(m))
  phys_features.append(Descriptors.SlogP_VSA7(m))
  phys_features.append(Descriptors.SlogP_VSA8(m))
  phys_features.append(Descriptors.SlogP_VSA9(m))
  phys_features.append(Descriptors.TPSA(m))
  phys_features.append(Descriptors.VSA_EState1(m))
  phys_features.append(Descriptors.VSA_EState10(m))
  phys_features.append(Descriptors.VSA_EState2(m))
  phys_features.append(Descriptors.VSA_EState3(m))
  phys_features.append(Descriptors.VSA_EState4(m))
  phys_features.append(Descriptors.VSA_EState5(m))
  phys_features.append(Descriptors.VSA_EState6(m))
  phys_features.append(Descriptors.VSA_EState7(m))
  phys_features.append(Descriptors.VSA_EState8(m))
  phys_features.append(Descriptors.VSA_EState9(m))
  phys_features.append(Descriptors.fr_Al_COO(m))
  phys_features.append(Descriptors.fr_Al_OH(m))
  phys_features.append(Descriptors.fr_Al_OH_noTert(m))
  phys_features.append(Descriptors.fr_ArN(m))
  phys_features.append(Descriptors.fr_Ar_COO(m))
  phys_features.append(Descriptors.fr_Ar_N(m))
  phys_features.append(Descriptors.fr_Ar_NH(m))
  phys_features.append(Descriptors.fr_Ar_OH(m))
  phys_features.append(Descriptors.fr_COO(m))
  phys_features.append(Descriptors.fr_COO2(m))
  phys_features.append(Descriptors.fr_C_O(m))
  phys_features.append(Descriptors.fr_C_O_noCOO(m))
  phys_features.append(Descriptors.fr_C_S(m))
  phys_features.append(Descriptors.fr_HOCCN(m))
  phys_features.append(Descriptors.fr_Imine(m))
  phys_features.append(Descriptors.fr_NH0(m))
  phys_features.append(Descriptors.fr_NH1(m))
  phys_features.append(Descriptors.fr_NH2(m))
  phys_features.append(Descriptors.fr_N_O(m))
  phys_features.append(Descriptors.fr_Ndealkylation1(m))
  phys_features.append(Descriptors.fr_Ndealkylation2(m))
  phys_features.append(Descriptors.fr_Nhpyrrole(m))
  phys_features.append(Descriptors.fr_SH(m))
  phys_features.append(Descriptors.fr_aldehyde(m))
  phys_features.append(Descriptors.fr_alkyl_carbamate(m))
  phys_features.append(Descriptors.fr_alkyl_halide(m))
  phys_features.append(Descriptors.fr_allylic_oxid(m))
  phys_features.append(Descriptors.fr_amide(m))
  phys_features.append(Descriptors.fr_amidine(m))
  phys_features.append(Descriptors.fr_aniline(m))
  phys_features.append(Descriptors.fr_aryl_methyl(m))
  phys_features.append(Descriptors.fr_azide(m))
  phys_features.append(Descriptors.fr_azo(m))
  phys_features.append(Descriptors.fr_barbitur(m))
  phys_features.append(Descriptors.fr_benzene(m))
  phys_features.append(Descriptors.fr_benzodiazepine(m))
  phys_features.append(Descriptors.fr_bicyclic(m))
  phys_features.append(Descriptors.fr_diazo(m))
  phys_features.append(Descriptors.fr_dihydropyridine(m))
  phys_features.append(Descriptors.fr_epoxide(m))
  phys_features.append(Descriptors.fr_ester(m))
  phys_features.append(Descriptors.fr_ether(m))
  phys_features.append(Descriptors.fr_furan(m))
  phys_features.append(Descriptors.fr_guanido(m))
  phys_features.append(Descriptors.fr_halogen(m))
  phys_features.append(Descriptors.fr_hdrzine(m))
  phys_features.append(Descriptors.fr_hdrzone(m))
  phys_features.append(Descriptors.fr_imidazole(m))
  phys_features.append(Descriptors.fr_imide(m))
  phys_features.append(Descriptors.fr_isocyan(m))
  phys_features.append(Descriptors.fr_isothiocyan(m))
  phys_features.append(Descriptors.fr_ketone(m))
  phys_features.append(Descriptors.fr_ketone_Topliss(m))
  phys_features.append(Descriptors.fr_lactam(m))
  phys_features.append(Descriptors.fr_lactone(m))
  phys_features.append(Descriptors.fr_methoxy(m))
  phys_features.append(Descriptors.fr_morpholine(m))
  phys_features.append(Descriptors.fr_nitrile(m))
  phys_features.append(Descriptors.fr_nitro(m))
  phys_features.append(Descriptors.fr_nitro_arom(m))
  phys_features.append(Descriptors.fr_nitro_arom_nonortho(m))
  phys_features.append(Descriptors.fr_nitroso(m))
  phys_features.append(Descriptors.fr_oxazole(m))
  phys_features.append(Descriptors.fr_oxime(m))
  phys_features.append(Descriptors.fr_para_hydroxylation(m))
  phys_features.append(Descriptors.fr_phenol(m))
  phys_features.append(Descriptors.fr_phenol_noOrthoHbond(m))
  phys_features.append(Descriptors.fr_phos_acid(m))
  phys_features.append(Descriptors.fr_phos_ester(m))
  phys_features.append(Descriptors.fr_piperdine(m))
  phys_features.append(Descriptors.fr_piperzine(m))
  phys_features.append(Descriptors.fr_priamide(m))
  phys_features.append(Descriptors.fr_prisulfonamd(m))
  phys_features.append(Descriptors.fr_pyridine(m))
  phys_features.append(Descriptors.fr_quatN(m))
  phys_features.append(Descriptors.fr_sulfide(m))
  phys_features.append(Descriptors.fr_sulfonamd(m))
  phys_features.append(Descriptors.fr_sulfone(m))
  phys_features.append(Descriptors.fr_term_acetylene(m))
  phys_features.append(Descriptors.fr_tetrazole(m))
  phys_features.append(Descriptors.fr_thiazole(m))  
  phys_features.append(Descriptors.fr_thiocyan(m))
  phys_features.append(Descriptors.fr_thiophene(m))
  phys_features.append(Descriptors.fr_unbrch_alkane(m))
  phys_features.append(Descriptors.fr_urea(m))
  
  return phys_features
  
  
#Input is the list of smile strings
def feature_matrix(smiles):
  for i in range(0,len(smiles)):
    a= phys_featurizer(smiles[i])
    