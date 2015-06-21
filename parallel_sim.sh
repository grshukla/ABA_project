#!/bin/bash


for k in $(seq 1 8); do
        mkdir par_prod$k
        mkdir par_prod$k/sim0
        cp sim$k/rst_1aba_prod$k.rst par_prod$k/sim0/rst_1aba_par${k}_prod0.rst
        cp 1aba_closed.top par_prod$k
        cp prod.in par_prod$k

        cd par_prod$k

        for i in $(seq 1 50); do

                mkdir sim$i
                cd sim$i
                j=$(expr $i - 1)


                echo "#!/bin/bash" >> prod.pbs
                echo "#PBS -l nodes=1:ppn=1:xk" >> prod.pbs
                echo "#PBS -l walltime=23:00:00" >> prod.pbs
                echo "#PBS -N 1aba_rec_par${k}_prod${i}" >> prod.pbs
                echo "#PBS -m abe" >> prod.pbs
                echo "#PBS -M sshukla4@illinois.edu" >> prod.pbs
                echo "#PBS -e errorfile.err" >> prod.pbs
                echo "#PBS -o output.out" >> prod.pbs
                echo "#PBS -q low" >> prod.pbs
                echo "#PBS -A jt3" >> prod.pbs
                echo "cd /u/sciteam/sshukla/scratch/mastersim/aba/rec_aba/1aba_closed_amd/par_prod$k/sim$i" >> prod.pbs
                echo "aprun -n 1 -N 1 pmemd.cuda -O -p ../1aba_closed.top -c ../sim$j/rst_1aba_par${k}_prod${j}.rst -i ../prod.in  -o out_1aba_par${k}_prod${i}.out -x mdcrd_1aba_par${k}_prod${i}.mdcrd -r rst_1aba_par${k}_prod${i}.rst" >> prod.pbs
                cd ..
        done
        cd ..
done

