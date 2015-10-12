from dataProcessing import *  
from textTester import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def fun(s):
    if s == 'n2':
        return [1,2,4,8]
    elif s == 'n3':
        return [1,3,9,27]
    elif s == 'kh1':
        return [1,2,3,4]
    elif s == 'kh2':
        return [2,4,6,8]
    elif s == 'kh3':
        return [7,8,9,10]
    elif s == 'kh4':
        return [5,7,11,13]

    return [1 , 2 , 3 , 4]


def startSimulation(request):
    if request.method == "GET":
        customerInterArrivalTime = fun(request.GET['customerInterArrivalTime'])
        ableServiceTime = fun(request.GET['ableServiceTime'])
        bakerServiceTime = fun(request.GET['bakerServiceTime'])
        
        if request.GET['ableBakerPriority'] == 'able' :
            ableBakerPriority = 0
        elif request.GET['ableBakerPriority'] == 'baker' :
            ableBakerPriority = 1
        elif request.GET['ableBakerPriority'] == 'rand':
            ableBakerPriority = 2

        if request.GET['selectCustomerOrTime'] == 'customerCount':
            selectCustomerOrTime = True
            customerCount = int(request.GET['value'])
            
        else:
            selectCustomerOrTime = False
            timeLength = int(request.GET['value'])

    # Data processing  -> MrHs
    if(selectCustomerOrTime):
        count = customerCount
    else:
        count = timeLength
    lili = customerGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, selectCustomerOrTime, count)
    
    
    # printing output using django -> Mahdi
    
    array2dOFRow = test(lili)
    
    
    return render(request, 'sim.html', {'allData': array2dOFRow})


def home(request):
    now = datetime.datetime.now()
    t = get_template('home.html')
    html = t.render(Context({'hhh': "hhh"}))
    return HttpResponse(html)
