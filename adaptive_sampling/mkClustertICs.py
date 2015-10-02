##########################################################################################
# This script make a cluster based on tICs and pick the less populated clusters, and find
# the frames in those clusters, the make a input file for Cpptraj to extract them
##########################################################################################
from msmbuilder.dataset import dataset
import numpy as np
from msmbuilder.cluster import KMeans
import pickle
import adptvSampling
import glob

myn_clusters = 200
n_samples = 100
# Load data file (input data for clusterring)
trajs = dataset('tica_trajs.h5')    
# make cluster of the tICs trajectories
cluster = KMeans(n_clusters=myn_clusters)
cluster.fit(trajs)
l = cluster.labels_

T = []
# the address should be the address of trajectories corresponding to dataset
for trj in glob.glob('longTrajs/*.mdcrd'):
	T.append(trj)
T.sort()
# Write the output file, which have the information about population of each cluster, 
# trajectory name and frame number of corresponding frame 	
adptvSampling.writeOPF(l, T, myn_clusters, n_samples)

# Based on information in output file, build the cpptraj input file, as you give it the topology name, it should be 
# common for all trajectories
topFile='mytopfile.top'
adptvSampling.CpptrajInGen(topFile)
#pickle.dump( cluster , open( "tICCluster.pkl", "wb"))
