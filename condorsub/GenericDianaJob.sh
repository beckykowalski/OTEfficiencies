#!/bin/bash
source /opt/exp_software/cuore/root/root_v5.34.36/bin/thisroot.sh
#cd /storage/gpfs_data/cuore/users/kowalski/OTEfficiency_Jan6_2022/cuoresw/cfg/CUORE_OT/
source /storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/setup.sh

#export CUORE_DB_HOST=dbfarm-2
#export CUORE_DB_PORT=35432
#export CUORE_DB_NAME=qdb
#export CUORE_DB_USER=cuore

## Print some environment variables to archive how they were set
echo "HOST IS " $HOSTNAME
printenv

/storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/bin/diana -C /storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/cfg/CUORE_OT/otefficiency_injected_pulses.cfg -l /storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/log/runREPLACERUN_towerREPLACETOWER.log -V TOWER REPLACETOWER -V RUN REPLACERUN -V DATASET 3519 -V MEASTYPE R -V SCRATCH /storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/scratch/ -V SHARED_SCRATCH /storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/scratch/ 

