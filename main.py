from dataProcessing import *  
from textTester import *                

def main():
    
   #Input data ->Mahdi
    customerInterArrivalTime = [1,2,3,4]  
    ableServiceTime = [5,6,7,8] 
    bakerServiceTime = [10,11,12,13] 
    ableBakerPriority = 0 #If 0 => Able is first if 1 => baker is first if 2 => randomly chosen
    
    selectCustomerOrTime = True #If true customer number is given if false time period is given
    
    customerCount = 100  
    timeLength = 0 
    
    
    
    # Data processing  -> MrHs
    if(selectCustomerOrTime):
        count = customerCount
    else:
        count = timeLength
    lili = customerGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, selectCustomerOrTime, count)
    
    
    # printing output using django -> Mahdi
    
    test(lili)
    
    return 0

main()