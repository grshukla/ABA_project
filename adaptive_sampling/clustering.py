from sklearn.cluster import KMeans
import numpy as np
import glob
import os
import cPickle as pickle
import pandas as pd
from msmbuilder.dataset import dataset
import adptvSampling
from sklearn.cluster import KMeans

##############################################################
#User defined variables
##############################################################
myn_clusters = 200
from_clusters=5
frame_per_cluster=10
traj_name='apo_aba_with_water.mdcrd'
top_name='apo_aba.top'

################################################################
#If we are using distance of the residues as the metric
################################################################

temp=pd.read_csv('lys_aba_distance.dat', sep='\s+')

dataset=temp.iloc[:,1]
dataset=np.array(dataset)
dataset=dataset.reshape(-1,1)

cluster = KMeans(n_clusters=myn_clusters)
cluster.fit(dataset)


centers=cluster.cluster_centers_
centers=centers.reshape(myn_clusters)

l=cluster.labels_
n_cluster = cluster.n_clusters

n_frames=len(dataset)
count_matrix = np.zeros(n_cluster)
for j in range(0,(n_frames)):
	cluster_id = l[j]
	count_matrix[cluster_id]= count_matrix[cluster_id] + 1

sorted_index= centers.argsort()


frames=[]
for i in range(from_clusters):
	frame_index=np.where(l==sorted_index[i])
	frame_index=np.array(frame_index)
	frame_length=len(frame_index[0])
	frame_index.resize(frame_length)
	frames.append(frame_index[0:frame_per_cluster].tolist())
	

frames=np.array(frames).reshape(from_clusters*frame_per_cluster)
cpp_frm=frames+1

for i in range(len(cpp_frm)):
	f = open('res_cpptraj'+ str(i+1) + '.in', 'w')
	f.write('parm ' + top_name  + '\n')
	f.write('trajin ' + traj_name  + '\n')
	f.write('parmbox alpha 90 beta 90 gamma 90\n')
	f.write('trajout par' + str(i+1) + '_sim0'+ '.rst restart onlyframes ' + str(cpp_frm[i]) +'\n')
	f.write('run \n')
	f.write('quit \n')
	f.close()

#Extracting one restart file from 189 GB dataset takes 1 hour 




 
