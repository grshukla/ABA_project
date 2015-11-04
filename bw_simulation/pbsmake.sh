#!/bin/bash

rec=pyl10   #Protein receptor type e.g. pyl10, pyl2
sys=apo_aba #name of system, name of topology file
par=50        #How many parallel simulation have to be launched
dir=/Users/Saurabh/mastersim/script_repository/bw_simulation
sim=3        #How many sequencial simulations are launched in one sequence
nsteps=30000000       #number of steps the simulation must be run
round=2

mkdir pbs_scripts rst_files run_folder traj_files input_files analysis

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

############ Copying npt rst file, if round 1 of adaptive sampling ################
#for k in $(seq 1 ${par});
#do
#	cp ../../npt/npt.rst rst_files/par${k}_sim0.rst
#done
###################################################################################


cd analysis

######################################################################
#######CPPtraj file for strpping and combining all trajectories#######
######################################################################
echo "parm ../${sys}.top"  >> strip_cpptraj.in

for i in $(seq 1 $par); do
	for j in $(seq 1 $sim); do 
		echo "trajin ../traj_files/par${i}_sim${j}.mdcrd" >> strip_cpptraj.in
	done 
done

echo "autoimage"  >> strip_cpptraj.in
echo "strip :WAT"  >> strip_cpptraj.in
echo "strip :Na+ outprefix stripped"  >> strip_cpptraj.in
echo "trajout ${rec}_${sys}_r${round}_stripped.mdcrd"  >> strip_cpptraj.in

######################################################################
#######CPPtraj file for  combining all trajectories###################
######################################################################

echo "parm ../${sys}.top"  >> combine_cpptraj.in

for i in $(seq 1 $par); do
        for j in $(seq 1 $sim); do
                echo "trajin ../traj_files/par${i}_sim${j}.mdcrd" >> combine_cpptraj.in
        done
done

echo "autoimage"  >> combine_cpptraj.in
echo "trajout ${rec}_${sys}_r${round}_combined.mdcrd"  >> combine_cpptraj.in

######################################################################
#######PBS files for combining the trajectories#######################
######################################################################
echo "#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=15:00:00
#PBS -N cpp_${rec}_${sys}
#PBS -q cse
#PBS -W group_list=chbe_diwakar

cd /home/sshukla4/scratch/newsim/${rec}/${sys}/prod/round${round}/analysis
/projects/cse/shared/diwakar/diwakar_software/amber14/bin/cpptraj -i combine_cpptraj.in" >> combine.pbs


echo "#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=15:00:00
#PBS -N cpp_${rec}_${system}
#PBS -q cse
#PBS -W group_list=chbe_diwakar

cd /home/sshukla4/scratch/newsim/${rec}/${sys}/prod/round${round}/analysis

/projects/cse/shared/diwakar/diwakar_software/amber14/bin/cpptraj -i strip_cpptraj.in" >> strip.pbs


######################################################################
#######CPPTRAJ featurization##########################################
######################################################################
if [ "$rec" = pyl10 ]; then
        if [ "$sys" = "apo_aba" ]; then
                echo "parm stripped.apo_aba.top" >> aba_site_pyl0_apo.in
                echo "trajin pyl10_apo_aba_r${round}_stripped.mdcrd" >> aba_site_pyl0_apo.in
                echo "distance PRO_GLY @1251 @1624 out pyl10_apo_distance.dat" >> aba_site_pyl0_apo.in
                echo "distance HIS_LEU @1650 @1691 out pyl10_apo_distance.dat" >> aba_site_pyl0_apo.in
                echo "distance LYS_ABA @793 @2728 out pyl10_apo_distance.dat" >> aba_site_pyl0_apo.in
        else
                echo "parm stripped.holo_aba.top" >> loop_rmsd_pyl10_holo.in
                echo "trajin pyl10_holo_aba_r${round}_stripped.mdcrd" >> loop_rmsd_pyl10_holo.in
                echo "rmsd :1-154 first" >> loop_rmsd_pyl10_holo.in
                echo "rmsd :23-37,55-62,66,82-94,113,131-139 first nofit out loop_rmsd_pyl10_holo.dat" >> loop_rmsd_pyl10_holo.in
        fi
else
        if [ "$sys" = "apo_aba" ]; then
                echo "parm stripped.apo_aba.top" >>aba_site_pyl2_apo.in
                echo "trajin pyl2_apo_aba_r${round}_stripped.mdcrd" >> aba_site_pyl2_apo.in
                echo "distance PRO_GLY @1439 @1813 out pyl2_apo_distance.dat" >> aba_site_pyl2_apo.in
                echo "distance HIS_LEU @1842 @1883 out pyl2_apo_distance.dat" >> aba_site_pyl2_apo.in
                echo "distance LYS_ABA @997 @5856 out pyl2_apo_distance.dat" >> aba_site_pyl2_apo.in

        else
                echo "parm stripped.holo_aba.top" >> loop_rmsd_pyl2_holo.in
                echo "trajin pyl2_holo_aba_r${round}_stripped.mdcrd" >> loop_rmsd_pyl2_holo.in
                echo "rmsd :1-181 first" >> loop_rmsd_pyl2_holo.in
                echo "rmsd :49-63,81-88,92,108-120,141,159-167 first nofit out loop_rmsd_pyl2_holo.dat" >> loop_rmsd_pyl2_holo.in
        fi
fi
