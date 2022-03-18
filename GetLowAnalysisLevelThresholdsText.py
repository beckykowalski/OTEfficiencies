
import os 
import sys

dataset = 3519

textfile10 = open("ds"+str(dataset)+"_10.txt", "w")
textfile15 = open("ds"+str(dataset)+"_15.txt", "w")


for i in range(1, 20):
    f = open("analysis_energy_thr_from_background_ds"+str(dataset)"_tower"+str(i).zfill(3)+".txt", "r")

    lines = f.readlines()
    
    for line in range(len(lines)):
        linevals = lines[line].split()
        channel = int(linevals[0])
        thr = float(linevals[1])
        
        if thr < 10. and thr > 0.:
            textfile10.write(str(channel)+"\n")

        if thr < 15. and thr > 0.:
            print(channel)
            textfile15.write(str(channel)+"\n")


