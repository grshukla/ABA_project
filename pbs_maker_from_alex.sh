#!/bin/bash

# Set the system name (ex. if the inpcrd file is ABC.prmtop, then sys=ABC)
sys=

# Set path to directory containing all input files and where output will be written to
dir=

# Set the number of runs
num=

# Set walltime
time="23:00:00"

for run in $(seq 0 $num); do
	crd=$(expr $run + 1)
	if [[ $run < 1 ]]; then
		res=''
	else
		res="_${run}" 
	fi
        echo "#!/bin/bash" >> ${sys}_${crd}.pbs
        echo "#PBS -l nodes=1:ppn=1:xk" >> ${sys}_${crd}.pbs
        echo "#PBS -l walltime=${time}" >> ${sys}_${crd}.pbs
        echo "#PBS -N ${sys}_${run}" >> ${sys}_${crd}.pbs
        echo "#PBS -e ${sys}_${run}.err" >> ${sys}_${crd}.pbs
        echo "#PBS -o ${sys}_${run}.out" >> ${sys}_${crd}.pbs
        echo "#PBS -q normal" >> ${sys}_${crd}.pbs
        echo "#PBS -A jt3" >> ${sys}_${crd}.pbs
        echo "" >> ${sys}_${crd}.pbs
        echo "cd ${dir}" >> ${sys}_${crd}.pbs
        echo "" >> ${sys}_${crd}.pbs
        echo "aprun -n 1 -N 1 pmemd.cuda -O -p ${sys}.prmtop -c ${sys}${res}.rst -i production.in -o ${sys}_${crd}.out -x ${sys}_${crd}.mdcrd -r ${sys}_${crd}.rst" >> ${sys}_${crd}.pbs
done
