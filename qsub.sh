#!/bin/bash
one=$(qsub sim21/prod.pbs)
echo $one
two=$(qsub -W depend=afterany:$one sim22/prod.pbs)
echo $two
three=$(qsub -W depend=afterany:$two sim23/prod.pbs)
echo $three
four=$(qsub -W depend=afterany:$three sim24/prod.pbs)
echo $four
five=$(qsub -W depend=afterany:$four sim25/prod.pbs)
echo $five
six=$(qsub -W depend=afterany:$five sim26/prod.pbs)
echo $six
seven=$(qsub -W depend=afterany:$six sim27/prod.pbs)
echo $seven
eight=$(qsub -W depend=afterany:$seven sim28/prod.pbs)
echo $eight
nine=$(qsub -W depend=afterany:$eight sim29/prod.pbs)
echo $nine
ten=$(qsub -W depend=afterany:$nine sim30/prod.pbs)
echo $ten
