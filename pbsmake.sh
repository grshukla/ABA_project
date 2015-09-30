#!/bin/bash

rec=pyl10   #Protein receptor type e.g. pyl10, pyl2
sys=apo_aba #name of system, name of topology file
par=20        #How many parallel simulation have to be launched
dir=/u/sciteam/sshukla/scratch/newsim/pyl10/apo_aba/prod/round1
sim=10        #How many sequencial simulations are launched in one sequence
nsteps=30000000       #number of steps the simulation must be run

mkdir pbs_scripts rst_files run_folder traj_files input_files

############ Input File ########################
cd input_files

for k in $(seq 1 ${par});
do
	echo "production (500000 = 1ns)
&cntrl
imin = 0, ntx = 1, irest = 0, nstlim = ${nsteps},
temp0 = 300, ig = $RANDOM,
ntc = 2, ntf = 2, ntt = 3, dt = 0.002, nscm=10000,
ntb = 2, ntp = 1, taup = 1.0, gamma_ln = 1.0,
ntwx = 10000, ntwe = 0, ntwr = 10000, ntpr = 10000,
cut = 10.0, iwrap = 1,
/" >> prod${k}.in
done


echo "production (500000 = 1ns)
&cntrl
imin = 0, ntx = 5, irest = 1, nstlim = ${nsteps},
temp0 = 300, ig = $RANDOM,
ntc = 2, ntf = 2, ntt = 3, dt = 0.002, nscm=10000,
ntb = 2, ntp = 1, taup = 1.0, gamma_ln = 1.0,
ntwx = 10000, ntwe = 0, ntwr = 10000, ntpr = 10000,
cut = 10.0, iwrap = 1,
/" >> prod.in




cd ${dir}


########## PBS Scripts ##########################
cd pbs_scripts

for k in $(seq 1 ${par}); 
do
        for i in $(seq 1 ${sim}); 
	do
                j=$(expr $i - 1)
		
		if [ $i = "1" ]; then
                	echo "#!/bin/bash" >> par${k}_sim${i}.pbs
                	echo "#PBS -l nodes=1:ppn=1:xk" >> par${k}_sim${i}.pbs
                	echo "#PBS -l walltime=23:00:00" >> par${k}_sim${i}.pbs
			echo "#PBS -o ${k}_${i}.out" >> par${k}_sim${i}.pbs
			echo "#PBS -e ${k}_${i}.err" >> par${k}_sim${i}.pbs
                	echo "#PBS -N ${k}_${i}_${rec}_${sys}" >> par${k}_sim${i}.pbs
                	echo "#PBS -q low" >> par${k}_sim${i}.pbs
                	echo "#PBS -A jt3" >> par${k}_sim${i}.pbs
                	echo "cd ${dir}/run_folder" >> par${k}_sim${i}.pbs
			echo "aprun -n 1 -N 1 pmemd.cuda -O -p ../${sys}.top -c ../rst_files/par${k}_sim${j}.rst -i ../input_files/prod${k}.in -o par${k}_sim${i}.out -x ../traj_files/par${k}_sim${i}.mdcrd -r ../rst_files/par${k}_sim${i}.rst" >> par${k}_sim${i}.pbs
		else
			echo "#!/bin/bash" >> par${k}_sim${i}.pbs
                        echo "#PBS -l nodes=1:ppn=1:xk" >> par${k}_sim${i}.pbs
                        echo "#PBS -l walltime=23:00:00" >> par${k}_sim${i}.pbs
                        echo "#PBS -N ${k}_${i}_${rec}_${sys}" >> par${k}_sim${i}.pbs
			echo "#PBS -o ${k}_${i}.out" >> par${k}_sim${i}.pbs
                        echo "#PBS -e ${k}_${i}.err" >> par${k}_sim${i}.pbs
                        echo "#PBS -q low" >> par${k}_sim${i}.pbs
                        echo "#PBS -A jt3" >> par${k}_sim${i}.pbs
                        echo "cd ${dir}/run_folder" >> par${k}_sim${i}.pbs
                        echo "aprun -n 1 -N 1 pmemd.cuda -O -p ../${sys}.top -c ../rst_files/par${k}_sim${j}.rst -i ../input_files/prod.in -o par${k}_sim${i}.out -x ../traj_files/par${k}_sim${i}.mdcrd -r ../rst_files/par${k}_sim${i}.rst" >> par${k}_sim${i}.pbs
		fi 
			        
	done
done

cd ${dir}

############ Copying npt rst file ################
for k in $(seq 1 ${par});
do
	cp ../../npt/npt.rst rst_files/par${k}_sim0.rst
done
