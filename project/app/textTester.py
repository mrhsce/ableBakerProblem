def test(lili):
        s = ""
        for i in range(len(lili)):
            k = lili[i]
            s = s  + str(i)+"  |  "+str(k.interArrivalTime)+"  |  "+str(k.arrivalTime)+"  |  "+str(k.whenAbleAvailable)+"  |  "+str(k.whenBakerAvailable)+"  |  "+str(k.serverChosen)+"  |  "+str(k.serviceTime)+"  |  "+str(k.timeServiceBegins)+"  |  "+str(k.ableServiceCompletedTime)+"  |  "+str(k.bakerServiceCompletedTime)+"  |  "+str(k.callerDelay)+"  |  "+str(k.timeInsystem)+"  |  " + "\n";
        return s