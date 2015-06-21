def cl_count(cluster):
        import numpy
        labels = cluster.labels_
        n_cluster = cluster.n_clusters
        trajs = len(labels)
        count_matrix = numpy.zeros(n_cluster)


        for i in range(0,(trajs)):
#               print "i value is %r" % i
                n_frames= len(labels[i])
#               print "frames in %r trajectory are %r" % (i,n_frames)
                for j in range(0,(n_frames)):
                        cluster_id = labels[i][j]
                        count_matrix[cluster_id]= count_matrix[cluster_id] + 1

        return count_matrix
