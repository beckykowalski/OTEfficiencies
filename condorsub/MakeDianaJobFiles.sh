#!/bin/bash

#for r in {350056..350079}
while IFS= read -r r
do 
    mkdir -p ds3519/Job_run$r
#    for t in {1..19}
    for t in {001..019}
    do 
	cp GenericDianaJob.sh ds3519/Job_run$r/DianaJob_run${r}_tower$t.sh
	cp GenericSubmissionScript.sub ds3519/Job_run$r/CondorSub_run${r}_tower$t.sub

	sed -i -e "s/REPLACERUN/$r/g" ds3519/Job_run$r/DianaJob_run${r}_tower$t.sh
	sed -i -e "s/REPLACETOWER/$t/g" ds3519/Job_run$r/DianaJob_run${r}_tower$t.sh

	sed -i -e "s/REPLACERUN/$r/g" ds3519/Job_run$r/CondorSub_run${r}_tower$t.sub
	sed -i -e "s/REPLACETOWER/$t/g" ds3519/Job_run$r/CondorSub_run${r}_tower$t.sub
	sed -i -e "s/REPLACEEX/DianaJob_run${r}_tower$t.sh/g" ds3519/Job_run$r/CondorSub_run${r}_tower$t.sub

    done
done < "/storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/workspace/ds3519_bkg_runs.txt"
