
import os 
import sys
import ROOT
import numpy as np

runlist = []
# set range to values runs in dataset
for i in range(350056, 350080):
    runlist.append(i)

def runInfolist(datapath, run, dataset):
    textfile7 = open("txtfiles/LessThanSeven/run"+str(run)+"_ds"+str(dataset)+"_7.txt", "w")
    textfile10 = open("txtfiles/LessThanTen/run"+str(run)+"_ds"+str(dataset)+"_10.txt", "w")

    count7 = 0
    count10 = 0

    f = open(datapath+"/run"+str(run)+"/chan_threshold_run"+str(run)+".txt")
    lines = f.readlines()[1:]
    
    for line in range(len(lines)):
        linevals = lines[line].split()
        channel = int(linevals[0])
        thr = float(linevals[1])
        
        if thr < 7. and thr > 0.:
            textfile7.write(str(channel) + " " + str(thr)+"\n")
            count7 += 1

        if thr < 10. and thr > 0.:
            textfile10.write(str(channel) + " " + str(thr)+"\n")
            count10 += 1

    textfile7.close()
    textfile10.close()


    return count7, count10


textfileCount = open("textfilesWithCounter/ds3519.txt", "w")

for r in runlist:
    print r
    
    l7, l10 = runInfolist("/storage/gpfs_data/cuore/users/kowalski/OTEff_Jan21_2022/cuoresw/pat/efficiencies/", r, 3519)

    textfileCount.write("Run "+str(r)+" has "+str(l7)+" bolometers < 7 keV and "+str(l10)+" bolometers < 10 keV\n")

textfileCount.close()
