import numpy as np
import scipy
import matplotlib.pyplot as plt

runlist = []
# set range to values runs in dataset ***Hardcoded**
for i in range(350191, 350230):
    runlist.append(i)
#print(runlist)

def runInfolist(run):
    ListOfChan = []
    f = open("chan_threshold_run"+str(run)+".txt")
    lines = f.readlines()[1:]
    for line in lines:
        linevals = line.split()
        channel = int(linevals[0])
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
    if len(ListOfChan) is not 988:
        for i in range(len(ListOfChan)):
            channelInList = ListOfChan[i,0]
            compare_ch=int(channelInList)
            iplus=i+1
            if channelInList != iplus:
                ListOfChan=np.insert(ListOfChan, i, [i+1,0], 0)
    f.close()
    return ListOfChan

#making plots for each tower
for t in range(1, 20):
    for r in runlist:
        rdata =  runInfolist(r)
        #print(rdata)
        rlistx = np.zeros(986)
        rlisty = np.zeros(986)
        #print(len(rdata))
        for ch in range(986):
            rlistx[ch] = (rdata[ch,0])
            rlisty[ch] = (rdata[ch,1])
        filter_arr = []
        chmin=(t-1)*52
        chmax=chmin+52
        for element in rlistx:
            if element>=chmin and element<chmax:
                filter_arr.append(True)
            else:
                filter_arr.append(False)
        t_rlistx=rlistx[filter_arr]
        t_rlisty=rlisty[filter_arr]
        plt.gca().scatter(t_rlistx, t_rlisty)
        #stop on last run ***Hardcoded**
        if r==350229:
            plt.xlabel("Channel Number")
            plt.ylabel("OT Thereshold (keV)")
            plt.title("tower"+str(t))
            plt.gcf().set_size_inches(10, 5)
            plt.ylim(0, 40)
            plt.savefig("tower"+str(t)+".png")
            plt.clf()

