qstat -u sshukla |grep "pyl10_holo" |cut -d"." -f1 |xargs qdel
