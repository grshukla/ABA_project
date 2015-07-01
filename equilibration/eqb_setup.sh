#!/bin/bash


mkdir npt_files nvt_files run_folder scripts topo_files traj_files


cd scripts

echo "eqb(2000000 steps = 1 ns)
&cntrl
 imin=0, irest=0,
 nstlim=5000000, dt=0.002,ig=-1,
 ntpr=5000, ntwx=5000,
 ntc=2, ntf=2, ntp=1,
 cut=10.0, ntb=2,
 ntt=3, gamma_ln=1.0,
 tempi=300.0, temp0=300.0,
 iwrap=1,nscm=5000,
/" >> npt.in

echo "#!/bin/bash


for i in $(seq 1 15); do

        echo "#!/bin/bash" >> npt$i.pbs
        echo "#PBS -l nodes=1:ppn=1:xk" >> npt$i.pbs
        echo "#PBS -l walltime=23:00:00" >> npt$i.pbs
        echo "#PBS -N npt_docking$i" >> npt$i.pbs
        echo "#PBS -m abe" >> npt$i.pbs
        echo "#PBS -q low" >> npt$i.pbs
        echo "#PBS -A jt3" >> npt$i.pbs
        echo "cd /u/sciteam/sshukla/scratch/mastersim/aba/docking/pyl2/eqb/run_folder" >> npt$i.pbs
        echo "aprun -n 1 -N 1 pmemd.cuda -O -p ../topo_files/pyl2_leap_$i.top -c ../nvt_files/nvt_$i.rst -i ../scripts/npt.in -o npt_$i.out -x ../traj_files/npt_$i.mdcrd -r ../npt_files/npt_$i.rst" >> npt$i.pbs
done" >>  pbsmaker_npt.sh





echo "#!/bin/bash


for i in $(seq 1 15); do

        qsub npt$i.pbs

done" >> qsub_npt.sh
