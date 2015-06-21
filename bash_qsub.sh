#!/bin/bash
one=$(qsub sim7/prod.pbs)
echo $one
two=$(qsub -W depend=afterany:$one sim8/prod.pbs)
echo $two
three=$(qsub -W depend=afterany:$two sim9/prod.pbs)
echo $three
four=$(qsub -W depend=afterany:$three sim10/prod.pbs)
echo $four
five=$(qsub -W depend=afterany:$four sim11/prod.pbs)
echo $five
six=$(qsub -W depend=afterany:$five sim12/prod.pbs)
echo $six
