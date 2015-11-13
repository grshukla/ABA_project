import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import cPickle as pkl
import os
from matplotlib.colors import LogNorm


f1='chembl_drugs.txt'
temp= pd.read_table(f1)
oral_drugs=temp[temp.ORAL=='Y']
oral_drugs=oral_drugs.dropna(subset=['CANONICAL_SMILES'])
