#!/bin/bash

i=3
echo $i 


echo "eqb(2000000 steps = 1 ns)
&cntrl
 imin$i=0, irest=0,
 nstlim=2000000, dt=0.002,ig=-1,
 ntpr=5000, ntwx=5000,
 ntc=2, ntf=2, ntp=1,
 cut=10.0, ntb=2,
 ntt=3, gamma_ln=1.0,
 tempi=300.0, temp0=300.0,
 iwrap=1,nscm=5000,
/" >> npt.in
