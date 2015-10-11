#!/bin/bash 

# I have two topology files monomer.top and dimer.top in the current folder. and dimer.rst and monomer.rst are the 
# restart files correspoding to topology.

echo "production (500000 = 1ns)
&cntrl
imin = 0, ntx = 5, irest = 1, nstlim = 100000000,
temp0 = 300, ig = $RANDOM,
ntc = 2, ntf = 2, ntt = 3, dt = 0.002, nscm=10000,
ntb = 2, ntp = 1, taup = 1.0, gamma_ln = 1.0,
ntwx = 10000, ntwe = 0, ntwr = 10000, ntpr = 10000,
cut = 10.0, iwrap = 1,
/" >> prod.in



for sys in monomer dimer
do
	for j in 1 8 16 32 64 128 256
	do      
		if [ $j -gt 10 ]
		then
			k=$(expr $j / 16)
		else 
			k=1
		fi
		mkdir ${j}_${sys}
		cd ${j}_${sys}
		echo "#!/bin/bash" >> ${j}_${sys}.slurm
		echo "#SBATCH -J ${j}_${sys}" >> ${j}_${sys}.slurm
		echo "#SBATCH -o ${j}_${sys}" >> ${j}_${sys}.slurm
		echo "#SBATCH -N $k" >> ${j}_${sys}.slurm
		echo "#SBATCH -n $j" >> ${j}_${sys}.slurm
		echo "#SBATCH -p normal" >> ${j}_${sys}.slurm
		echo "#SBATCH -t 02:00:00" >> ${j}_${sys}.slurm
		echo "module use /work/01114/jfonner/public/modules/modulefiles" >> ${j}_${sys}.slurm
		echo "module load intel/15.0.2" >> ${j}_${sys}.slurm
		echo "module load python/2.7.9" >> ${j}_${sys}.slurm
		echo "module load amber/14.0" >> ${j}_${sys}.slurm
		echo "ibrun sander.MPI -O -i ../prod.in -p ../${sys}.top -c ../${sys}.rst -r  ${j}_${sys}.rst -o ${j}_${sys}.out -x ${j}_${sys}.mdcrd"  >> ${j}_${sys}.slurm
		sbatch ${j}_${sys}.slurm
		cd ..
	done
done
