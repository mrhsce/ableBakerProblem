# This class holds the information of a CallerMacro

class Caller():
    
    interArrivalTime = 0
    arrivalTime = 0
    whenAbleAvailable = 0
    whenBakerAvailable = 0
    serverChosen = 0   # 0 is able and 1 is baker
    serviceTime = 0
    timeServiceBegins = 0
    ableServiceCompletedTime = 0
    bakerServiceCompletedTime = 0
    callerDelay = 0
    timeInsystem = 0
    
    
    def __init__(self,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11):
        self.interArrivalTime = i1
        self.arrivalTime = i2
        self.whenAbleAvailable = i3
        self.whenBakerAvailable = i4
        self.serverChosen = i5
        self.serviceTime = i6
        self.timeServiceBegins = i7
        self.ableServiceCompletedTime = i8
        self.bakerServiceCompletedTime = i9
        self.callerDelay = i10
        self.timeInsystem = i11
        
        