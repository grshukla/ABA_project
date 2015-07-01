#!/bin/bash

echo "parm nife2.top"  >> cpptraj2.in 


for i in $(seq 1 21); do 
	echo "trajin ../../sim${i}/mdcrd_amd_nife_prod${i}.mdcrd 1 last 20" >> cpptraj2.in
done


echo "autoimage"  >> cpptraj2.in
echo "strip :WAT outprefix strippedwater"  >> cpptraj2.in
echo "strip :Na+ outprefix stripped_water_Na"  >> cpptraj2.in
echo "trajout output.mdcrd"  >> cpptraj2.in



