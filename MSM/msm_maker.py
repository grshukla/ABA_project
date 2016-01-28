from sklearn.cluster import KMeans
from msmbuilder.msm import MarkovStateModel
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
import cPickle as pkl
import pandas as pd


#Replicating the website example
temp=pd.read_csv('pyl10_apo_distance_r6.dat',sep='\s+')
dataset= np.array(temp)
dataset=dataset[:,1:4]


msmts0, msmts1 = {}, {}
lag_times = [1, 10, 20, 30, 40]
n_states = [4, 8, 16, 32, 64]

# Plot of timescales vs lag-time for checking convergence of MSM
for n in n_states:
    msmts0[n] = []
    msmts1[n] = []
    for lag_time in lag_times:
        assignments = KMeans(n_clusters=50).fit_predict(dataset)
        msm = MarkovStateModel(lag_time=lag_time, verbose=False).fit(assignments)
        timescales = msm.timescales_
        msmts0[n].append(timescales[0])
        msmts1[n].append(timescales[1])
        print('n_states=%d\tlag_time=%d\ttimescales=%s' % (n, lag_time, timescales[0:2]))
    print()
