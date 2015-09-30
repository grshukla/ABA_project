#!/bin/bash





for i in $(seq 21 50); do

        mkdir sim$i
        cd sim$i
        j=$(expr $i - 1)


        echo "#!/bin/bash" >> prod.pbs
        echo "#PBS -l nodes=1:ppn=1:xk" >> prod.pbs
        echo "#PBS -l walltime=24:00:00" >> prod.pbs
        echo "#PBS -N rec_prod$i" >> prod.pbs
        echo "#PBS -m abe" >> prod.pbs
        echo "#PBS -M sshukla4@illinois.edu" >> prod.pbs
        echo "#PBS -e errorfile.err" >> prod.pbs
        echo "#PBS -o output.out" >> prod.pbs
        echo "#PBS -q normal" >> prod.pbs
        echo "#PBS -A jt3" >> prod.pbs
        echo "cd /u/sciteam/sshukla/scratch/mastersim/aba/rec_only/production_files/sim$i" >> prod.pbs
        echo "aprun -n 1 -N 1 pmemd.cuda -O -p ../aba.top -c ../sim$j/rst_aba_prod$j.rst -i ../prod.in  -o out_aba_prod$i.out -x mdcrd_aba_prod$i.mdcrd -r rst_aba_prod$i.rst" >> prod.pbs
        cd ..
done
~      

