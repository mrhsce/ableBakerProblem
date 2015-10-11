from caller import *
import random

def getInterArrivalTime(customerList):
    pass
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
    pass

def customerGenerator(customerList,ableList,bakerList,priority,customerOrTime,count):
    
    customreList = list()
    
    if(customerOrTime):
        for i in range(count):
            if(len(customerList) == 0):    # The fist caller
                if(priority == 2):
                    priority = select = random.choice([0,1])
                if(priority == 0):
                    servTime = random.choice(ableList)
                    customerList.append(Caller(0,0,0,0,0,servTime,0,servTime,0,0,0))
                if(priority == 1):
                    servTime = random.choice(bakerList)
                    customerList.append(Caller(0,0,0,0,1,servTime,0,0,servTime,0,0))                
            else:
                if(priority == 2):
                    priority = select = random.choice([0,1])
                if(priority == 0):
                    ableBaker = getAbleOrBaker(customerList[len(customerList)-1].whenAbleAvailable, customerList[len(customerList)-1].whenBakerAvailable, priority)
                    customerList.append(Caller(0,0,0,0,0,servTime,0,servTime,0,0,0))
                if(priority == 1):
                    servTime = random.choice(bakerList)
                    customerList.append(Caller(0,0,0,0,1,servTime,0,0,servTime,0,0))
                    



def main():
    
    #Input data ->Mahdi
    "در این قسمت باید از طریق یک اسپینر و یا هر ویو دیگری که صلاح میدانی این دیتا ها از کاربر گرفته شود "
    customerInterArrivalTime = list()  
    "توزیع آماری زمان رسیدن مشتری جدید"
    ableServiceTime = list() 
    "توزیع آماری زمان سرویس دهی ابل"
    bakerServiceTime = list() 
    "توزیع آماری زمان سرویس دهی بیکر"
    ableBakerPriority = 0 #If 0 => Able is first if 1 => baker is first if 2 => randomly chosen
    "این قسمت یک بولین است که از کاربر پرسیده می شود آیا می خواهد زمان بدهد و یا تعداد کل مشتری ها"
    
    selectCustomerOrTime = True #If true customer number is given if false time period is given
    
    customerCount = 0  
    "تعداد کل مشتری ها"
    timeLength = 0 
    "زمان کل شبیه سازی"
    
    
    
    # Data processing  -> MrHs
    
    
    # printing output using django -> Mahdi
    
    
    return 0

main()