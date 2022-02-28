#!/bin/bash 

for t in {001..019}
do
    condor_submit -spool -name sn-02 CondorSub_run350079_tower$t.sub
done 
