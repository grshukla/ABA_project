#!/bin/bash

system=holo_aba
pbspath=/home/sshukla4/scratch/newsim/pyl10/holo_aba

################Minimization Script##########
echo "Minimize
&cntrl
        imin=1,
        ntx=1,
        irest=0,
        maxcyc=10000,
        ncyc=1000,
        ntpr=1000,
        ntwx=0,
        cut=8.0,
        /" >> min.in

###############NVT Script ##################
echo "eqb(200000 steps = 100 ps)
&cntrl
 imin=0, irest=0,
 nstlim=10000, dt=0.002,ig=-1,
 ntpr=5000, ntwx=5000,
 ntc=2, ntf=2, ntp=0,
 cut=10.0, ntb=1,
 ntt=3, gamma_ln=1.0,
 tempi=0.0, temp0=300.0,
 iwrap=1,nscm=5000,
/" >> nvt.in

############## Min PBS ########################
echo "#!/bin/bash
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=1
#PBS -N ${system}_min
#PBS -q cse
#PBS -W group_list=chbe_diwakar

cd $pbspath

sander  -O  -i min.in  -o min_${system}.out  -c ${system}.crd -p ${system}.top -r min_${system}.rst" >> min.pbs


############## NVT PBS ##########################

echo "#!/bin/bash
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=1
#PBS -N ${system}_nvt
#PBS -q cse
#PBS -W group_list=chbe_diwakar

cd $pbspath

sander  -O  -i nvt.in  -o nvt_${system}.out  -c min_${system}.rst -p ${system}.top -r nvt_${system}.rst" >> nvt.pbs


############# Submission script ################
echo "#!/bin/bash
one=\$(qsub min.pbs)
echo \$one
two=\$(qsub -W depend=afterany:\$one nvt.pbs)
echo \$two" >> qsub.sh




bash qsub.sh
