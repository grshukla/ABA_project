import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import cPickle as pkl
import os
from matplotlib.colors import LogNorm


f1='chembl_drugs.txt'               #File name 
temp= pd.read_table(f1)            
oral_drugs=temp[temp.ORAL=='Y']     #Retaining only orally administered drugs
oral_drugs=oral_drugs.dropna(subset=['CANONICAL_SMILES'])   #Removing the columns which are "NaN" for smiles

#Loading the dataset
g= open('oral_drugs.pkl', 'rb')
oral_drugs=pkl.load(g)
g.close()


