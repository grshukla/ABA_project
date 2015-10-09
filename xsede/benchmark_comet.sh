#!/bin/bash 


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
	for j in 1 12 24 48 72 96 120 192 240
	do      
		if [ $j -gt 30 ]
		then
			k=$(expr $j / 24)
			l=24
		else 
			k=1
			l=${j}
		fi
		mkdir ${j}_${sys}
		cd ${j}_${sys}
		echo "#!/bin/bash" >> ${j}_${sys}.slurm
		echo "#SBATCH --job-name="${j}_${sys}"" >> ${j}_${sys}.slurm
		echo "#SBATCH --output="${j}_${sys}"" >> ${j}_${sys}.slurm
		echo "#SBATCH --nodes=$k" >> ${j}_${sys}.slurm
		echo "#SBATCH --ntasks-per-node=${l}" >> ${j}_${sys}.slurm
		echo "#SBATCH -A uic323" >> ${j}_${sys}.slurm
		echo "#SBATCH --partition=compute" >> ${j}_${sys}.slurm
		echo "#SBATCH -t 02:00:00" >> ${j}_${sys}.slurm
		echo "#SBATCH --export=ALL" >> ${j}_${sys}.slurm
		echo "module load amber" >> ${j}_${sys}.slurm
		echo "ibrun sander.MPI -O -i ../prod.in -p ../${sys}.top -c ../${sys}.rst -r  ${j}_${sys}.rst -o ${j}_${sys}.out -x ${j}_${sys}.mdcrd"  >> ${j}_${sys}.slurm
		sbatch ${j}_${sys}.slurm
		cd ..
	done
done
