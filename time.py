from datetime import datetime
from num2words import num2words

def militaryTime(time):
    timeObj = datetime.strptime(time, "%I:%M%p")
    hour = timeObj.hour
    min = timeObj.minute

    if(hour<10):
        hourstr="zero "+ num2words(hour)
    else:
        hourstr=num2words(hour)
    if(min==0):
        minstr="hundred hours"
    elif(min<10):
        minstr="zero "+num2words(min)
    else:
        minstr=num2words(min)

    
    print(hourstr,minstr)

    
militaryTime("5:05PM")

#time = input("What time is it? ")
#milTime = militaryTime(time)

