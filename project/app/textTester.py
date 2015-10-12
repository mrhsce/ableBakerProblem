from copy import copy, deepcopy
def test(lili):
        allData = []
        for i in range(len(lili)):
            k = lili[i]
            s = [str(i),str(k.interArrivalTime),str(k.arrivalTime),str(k.whenAbleAvailable),str(k.whenBakerAvailable),str(k.serverChosen),str(k.serviceTime),str(k.timeServiceBegins),str(k.ableServiceCompletedTime),str(k.bakerServiceCompletedTime),str(k.callerDelay),str(k.timeInsystem)];
            allData.append(deepcopy(s))
        return allData
