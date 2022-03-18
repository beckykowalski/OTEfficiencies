import numpy as np
import scipy
import matplotlib.pyplot as plt

runlist = []
# set range to values runs in dataset ***Hardcoded**
for i in range(350056, 350080):
    runlist.append(i)
#print(runlist)

def runInfolist(run):
    ListOfChan = []
    f = open("threshtexts/chan_threshold_run"+str(run)+".txt")
    lines = f.readlines()[1:]
    for line in lines:
        linevals = line.split()
        channel = int(linevals[0])
#        print ("channel "+str(channel)+" is on floor "+str(channel%13))
        thr = float(linevals[1])
        chmin = 1
        chmax = 988
        if channel >= chmin and channel <= chmax:
           ListOfChan.append([channel, thr])
    NewListOfChan=[]
    columnIndex=0
    ListOfChan=np.array(ListOfChan)
    #sorting channels
    ListOfChan=ListOfChan[ListOfChan[:,columnIndex].argsort()]
    if len(ListOfChan) is not 52:
        for i in range(len(ListOfChan)):
            channelInList = ListOfChan[i,0]
            compare_ch=int(channelInList)
            iplus=i+1
            if channelInList != iplus:
                ListOfChan=np.insert(ListOfChan, i, [i+1,0], 0)
    f.close()
    return ListOfChan

def towerInfolist():
    ListOfChan = []
    for t in range(1, 20):
        f = open("analysisthresh/analysis_energy_thr_from_background_ds3519_tower"+str(t).zfill(3)+".txt")
        lines = f.readlines()
        for line in lines:
            linevals = line.split()
            channel = int(linevals[0])
            thr = float(linevals[1])
            chi2 = float(linevals[2])
            chmin = 1
            chmax = 988
            if channel >= chmin and channel <= chmax:
                ListOfChan.append([channel, thr])
            NewListOfChan=[]
            columnIndex=0
    ListOfChan=np.array(ListOfChan)
    #sorting channels
    ListOfChan=ListOfChan[ListOfChan[:,columnIndex].argsort()]

    f.close()
    return ListOfChan


#making plots for each tower
for f in range(1, 14):
    count = 0

    tdata = towerInfolist()
    tlistx = np.zeros(len(tdata))
    tlisty = np.zeros(len(tdata))
    for ch in range(len(tdata)):
        tlistx[ch] = (tdata[ch, 0])
        tlisty[ch] = (tdata[ch, 1])

    chmin = 1
    chmax = 988

    FilterAnalysis = []

    for element in tlistx:
        if element%13 == float(f) or (element%13==0 and f is 13):
            FilterAnalysis.append(True)
        else:
            FilterAnalysis.append(False)
    analysisChannels = tlistx[FilterAnalysis]
    analysisThresh = tlisty[FilterAnalysis]
    
    plt.gca().scatter(analysisChannels, analysisThresh, marker = "v", s=100, color="black")

    for r in runlist:

        
        rdata =  runInfolist(r)
        rlistx = np.zeros(len(rdata))
        rlisty = np.zeros(len(rdata))
        #print(len(rdata))
        for ch in range(len(rdata)):
            rlistx[ch] = (rdata[ch,0])
            rlisty[ch] = (rdata[ch,1])
        filter_arr = []

        for element in rlistx:
            if element%13 == float(f) or (element%13==0 and f is 13): 
                filter_arr.append(True)
            else:
                filter_arr.append(False)
        t_rlistx=rlistx[filter_arr]
        t_rlisty=rlisty[filter_arr]
        
        plt.gca().scatter(t_rlistx, t_rlisty)
        #stop on last run ***Hardcoded**
        if r==350079:
            plt.xlabel("Channel Number")
            plt.ylabel("Thereshold (keV)")
            plt.title("floor "+str(f))
            plt.gcf().set_size_inches(10, 5)
            plt.ylim(0, 60)
#            plt.legend(loc="upper right", ncol=3)
            plt.savefig("floor"+str(f)+".png")
            plt.clf()

