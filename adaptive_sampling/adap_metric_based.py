from sklearn.cluster import KMeans
import numpy as np
import glob
import os
import cPickle as pickle
import pandas as pd
from sklearn.cluster import KMeans

##############################################################
#User defined variables
##############################################################
rec='pyl2'
sys='apo_aba'
myn_clusters = 200                       # Total number of clusters
from_clusters=5                          # Restart files making from clusters 
frame_per_cluster=10                     # Number of frames extracted from each cluster
traj_name='apo_aba_with_water.mdcrd'     
top_name='apo_aba.top'
path='/home/sshukla4/scratch/newsim/pyl10/apo_aba/prod/round1/combined_traj'
d_file_name='lys_aba_distance.dat'

################################################################
#If we are using distance of the residues as the metric
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


################################################################
#Saving the trajectory number matrix
################################################################
f = open('frames.pkl','wb’)
pickle.dump(cpp_frm,f)
f.close()



################################################################
#Writing cpptraj input files
################################################################
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

################################################################
#PBS Scripts 
################################################################
for i in range(len(cpp_frm)):
        f = open('res_'+ str(i+1) + '.pbs', 'w')
        f.write('#!/bin/bash'+ '\n')
        f.write('#PBS -l walltime=04:00:00'+ '\n')
        f.write('#PBS -l nodes=1:ppn=1'+ '\n')
        f.write('#PBS -N rst_'+ str(i+1)+ '\n')
        f.write('#PBS -q secondary'+ '\n')
        f.write('#PBS -W group_list=chbe_diwakar'+ '\n')
	f.write('cd '+ path+ '\n')
	f.write('cpptraj -i res_cpptraj' + str(i+1) + '.in'+ '\n')
        f.close()


################################################################
#Submission Script       
################################################################
f = open('submission_rst.sh', 'w')
f.write('#!/bin/bash'+ '\n')
f.write('for i in $(seq 1 '+ str(len(cpp_frm)) +'); do'+ '\n')
f.write('	qsub res_${i}.pbs'+ '\n')
f.write('done'+ '\n')
f.close()

################################################################
#Ledger
################################################################
f = open('ledger.txt', 'w')
f.write('Receptor is '+ rec + '\n')
f.write('system is '+ sys + '\n')
#f.write('number of frames in trajectory is '+ str(len(dataset) + '\n')
#f.write('Total clusters made are '+ str(myn_clusters) + '\n')
#f.write('Frames per cluster selected '+ str(frame_per_cluster) + '\n')
#f.write('Frames are selected from first '+ str(from_clusters) + 'clusters'+ '\n')
f.write('Cluster centers are given in acsending order' + str(centers[sorted_index]) + '\n')
f.write('Indexes of these clusters are' + str(sorted_index) + '\n')
f.write('frames selected are' + '\n' + str(cpp_frm) + + '\n' )
f.close()


