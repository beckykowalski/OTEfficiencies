###########################################################################################################################
# Creates text file of channels that are below a desired energy analysis threshold 
# Analysis threshold determined by algorithm described in
# https://docdb.wlab.yale.edu/cuore/RetrieveFile?docid=1959&filename=analysis_energy_thresholds_in_CUORE.pdf&version=1
# runs with:
# python GetLowAnalysisLevelThresholdsText.py -D <int_dataset> -T <double_desired_threshold> -P <string_path_to_data>
###########################################################################################################################


import os 
import sys
import argparse 

parser = argparse.ArgumentParser(description='makes file of low analysis thresholds')
parser.add_argument('datas', metavar = '-D', type = int)
parser.add_argument('threshlevel', metavar = '-T', type = float)
parser.add_argument('datapath', metavar = '-P', type = str)

args, unknown = parser.parse_known_args()

def GetChannelsWithLowThresholds(dataset, thresholdlevel, pathtodatafile):

    
    textfile = open("ds"+str(dataset)+"_Channels_with_Low_Aanalysis_thresholds.txt", "w")
    
    for i in range(1, 20):
        f = open(pathtodatafile+"analysis_energy_thr_from_background_ds"+str(dataset)+"_tower"+str(i).zfill(3)+".txt", "r")
        
        lines = f.readlines()
        
        for line in range(len(lines)):
            linevals = lines[line].split()
            channel = int(linevals[0])
            thr = float(linevals[1])
        
            if thr < thresholdlevel and thr > 5.:
                textfile.write(str(channel)+"\n")

    textfile.close()

GetChannelsWithLowThresholds(args.datas, args.threshlevel, args.datapath)
