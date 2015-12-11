from sklearn.cluster import KMeans
import numpy as np
import glob
import os
import cPickle as pickle
import pandas as pd

##############################################################
#User defined variables
##############################################################
rec='pyl2'
sys='holo_aba'
myn_clusters =200                       # Total number of clusters
from_clusters=50                          # Restart files making from clusters 
frame_per_cluster=1                     # Number of frames extracted from each cluster
traj_name='pyl5_apo_aba_r1_combined.mdcrd'     
top_name='apo_aba.top'
path='/scratch/users/sshukla4/newsim/pyl5/apo_aba/prod/round1/analysis/round3_rst'
d_file_name='pyl5_apo_distance_r1.dat'


################################################################
#Reading the cpptraj file for reading the trajectotries
################################################################
temp=pd.read_csv(d_file_name, sep='\s+')

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

sorted_index = count_matrix.argsort()

frames=[]
for i in range(from_clusters):
	frame_index=np.where(l==sorted_index[i])
	frame_index=np.array(frame_index)
	frames.append(frame_index[0][0].tolist())	

frames=np.array(frames).reshape(from_clusters*frame_per_cluster)
cpp_frm=frames+1

################################################################
#Saving the trajectory number matrix
################################################################
f = open('frames.pkl','wb')
pickle.dump(cpp_frm,f)
f.close()

################################################################
#Writing cpptraj input files
################################################################
f = open('res_cpptraj.in', 'wb')
f.write('parm ' + top_name  + '\n')
f.write('trajin ' + traj_name  + '\n')
f.write('parmbox alpha 90 beta 90 gamma 90\n')
for i in range(len(cpp_frm)):
	f.write('trajout par' + str(i+1) + '_sim0'+ '.rst restart onlyframes ' + str(cpp_frm[i]) +'\n')
f.write('run \n')
f.write('quit \n')
f.close()

#Extracting one restart file from 189 GB dataset takes 1 hour 

################################################################
#PBS Scripts 
################################################################
#for i in range(len(cpp_frm)):
#        f = open('res_'+ str(i+1) + '.pbs', 'w')
#        f.write('#!/bin/bash'+ '\n')
#        f.write('#PBS -l walltime=04:00:00'+ '\n')
#        f.write('#PBS -l nodes=1:ppn=1'+ '\n')
#        f.write('#PBS -N rst_'+ str(i+1)+ '\n')
 #       f.write('#PBS -q secondary'+ '\n')
  #      f.write('#PBS -W group_list=chbe_diwakar'+ '\n')
#	f.write('cd '+ path+ '\n')
#	f.write('cpptraj -i res_cpptraj' + str(i+1) + '.in'+ '\n')
 #       f.close()

################################################################
#Submission Script       
################################################################
#f = open('submission_rst.sh', 'w')
#f.write('#!/bin/bash'+ '\n')
#f.write('for i in $(seq 1 '+ str(len(cpp_frm)) +'); do'+ '\n')
#f.write('	qsub res_${i}.pbs'+ '\n')
#f.write('done'+ '\n')
#f.close()
