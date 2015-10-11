from caller import *
import random

def getInterArrivalTime(customerList):
    return random.choice(customerList)
def getAbleOrBaker(ableAvailTime,bakerAvailTime,priority):
    if(ableAvailTime == bakerAvailTime):
        if(priority == 2):
            select = random.choice([0,1])
            return select
        else:
            return priority 
    else:
        if(ableAvailTime < bakerAvailTime):
            return 0
        else:
            return 1    
def getServiceTime(ableOrBaker,ableList,bakerList):
    if(ableOrBaker == 0):
        return random.choice(ableList)
    else:
        return random.choice(bakerList)

def customerGenerator(customerTimeList,ableList,bakerList,priority,customerOrTime,count):
    
    customerList = list()
    
    if(customerOrTime):
        for i in range(count):
            if(len(customerList) == 0):    # The fist caller
                if(priority == 2):
                    priority  = random.choice([0,1])
                if(priority == 0):
                    servTime = random.choice(ableList)
                    customerList.append(Caller(0,0,0,0,0,servTime,0,servTime,0,0,0))
                if(priority == 1):
                    servTime = random.choice(bakerList)
                    customerList.append(Caller(0,0,0,0,1,servTime,0,0,servTime,0,0))                
            else:
                interArrVlTime = getInterArrivalTime(customerTimeList)
                timeInSystem = customerList[len(customerList)-1].arrivalTime
                if(priority == 2):
                    priority  = random.choice([0,1])
                ableBaker = getAbleOrBaker(customerList[len(customerList)-1].ableServiceCompletedTime, customerList[len(customerList)-1].bakerServiceCompletedTime, priority)
                servTime = getServiceTime(ableBaker, ableList, bakerList)
                
                if(ableBaker == 0):                    
                    arrivalTime = customerList[len(customerList)-1].arrivalTime + interArrVlTime
                    whenAbleAvailable = customerList[len(customerList)-1].ableServiceCompletedTime
                    whenBakerAvailableTime = customerList[len(customerList)-1].bakerServiceCompletedTime
                    
                    if(arrivalTime > whenAbleAvailable):
                        whenServiceBegins = arrivalTime
                    else:
                        whenServiceBegins = whenAbleAvailable
                    
                    if(arrivalTime < whenServiceBegins):
                        delay = whenServiceBegins - arrivalTime
                    else:
                        delay = 0 
                    customerList.append(Caller(interArrVlTime,arrivalTime,whenAbleAvailable,whenBakerAvailableTime,0,servTime,whenServiceBegins,whenAbleAvailable + servTime,whenBakerAvailableTime,delay,timeInSystem))
                if(ableBaker == 1):
                    arrivalTime = customerList[len(customerList)-1].arrivalTime + interArrVlTime
                    whenAbleAvailable = customerList[len(customerList)-1].ableServiceCompletedTime
                    whenBakerAvailableTime = customerList[len(customerList)-1].bakerServiceCompletedTime
                    
                    if(arrivalTime > whenBakerAvailableTime):
                        whenServiceBegins = arrivalTime
                    else:
                        whenServiceBegins = whenBakerAvailableTime
                    
                    if(arrivalTime < whenServiceBegins):
                        delay = whenServiceBegins - arrivalTime
                    else:
                        delay = 0        
                    customerList.append(Caller(interArrVlTime,arrivalTime,whenAbleAvailable,whenBakerAvailableTime,1,servTime,whenServiceBegins,whenAbleAvailable,whenBakerAvailableTime + servTime,delay,timeInSystem))
    else:
        pass
    
    return customerList                