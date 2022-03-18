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
count = 0

tdata = towerInfolist()
tlistx = np.zeros(len(tdata))
tlisty = np.zeros(len(tdata))
for ch in range(len(tdata)):
    tlistx[ch] = (tdata[ch, 0])
    tlisty[ch] = (tdata[ch, 1])
    
chmin = 1
chmax = 988
    
counts, bins, extra = plt.hist(tlisty, bins=100)
plt.xlabel("Analysis Threshold (keV)")
plt.ylabel("# Channels")
plt.yscale('log')
plt.gcf().set_size_inches(5, 5)
plt.savefig("testAnalysisThreshHist_log.png")
    
bigrundatalist = []

for r in runlist:
    
    rdata =  runInfolist(r)
    rlistx = np.zeros(len(rdata))
    rlisty = np.zeros(len(rdata))
    #print(len(rdata))
    for ch in range(len(rdata)):
        rlistx[ch] = (rdata[ch,0])
        rlisty[ch] = (rdata[ch,1])
    for v in rlisty:
        bigrundatalist.append(v)

#for i in bigrundatalist:
#    print (i)


xeff = np.linspace(1, 40, 39)
yeff = []
xeffl = []
yeffanalysis = []


for x in xeff:
    xeffl.append(x)
    count = 0
    countA = 0
    for i in bigrundatalist:
        if i < x and i > 0.:
            count +=1
    yeff.append(float(count)/(984.*24.))
    for i in tlisty:
        if i < x and i > 0.:
            countA += 1
            if i < 5. and x < 6.:
                print("threshold is "+str(i))
    yeffanalysis.append(float(countA)/984.)
    arrayOfRunData = np.zeros(len(bigrundatalist))
countOver = 0
for i in range(len(bigrundatalist)):
    if bigrundatalist[i] > 0. and bigrundatalist[i] < 200.:
        arrayOfRunData[i] = bigrundatalist[i]
    else:
        countOver+=1
        
#plt.scatter(xeff, yeff, label="OT")
#plt.scatter(xeff, yeffanalysis, label="analysis")
#plt.xlabel("OT Threshold ds3519 (keV)")
#plt.ylabel("Ch-run pairs below threshold (Normalized to 1)")
#plt.legend(loc='upper left')
#plt.savefig("threshBelowEff.png")

#plt.hist(arrayOfRunData, bins=100)
#plt.xlabel("OT Threshold (keV) (all runs ds3519)")
#plt.ylabel("# Channels")
#plt.yscale('log')
#plt.text(80, 2500, f'Overflow={countOver} ch-run pairs')
#plt.savefig("otThreshhist_log.png")
