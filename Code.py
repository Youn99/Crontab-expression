import unittest
import re  

def verify(crontab_parameter: str) -> str:
    """
    verify function
     check if the crontab parameters are correct => you can see the web site here https://crontab.guru/ .
     you need to follow the order of the schedule expression like in the web site: (minute, hour, day_month, month, day_week)
     the parameters are: 
     day_week: need to be * or 7.
     month: need to be * or 12.
     day_month: need to be * or 31.
     hour: need to be * or 23.
     minute: need to be * or 59.
     *: is equal to None.
    Parameter:
     crontab_parameter => need to be a string.
    Return:
      if the parameters are correct or not.
    
    """ 
    splitting = re.split(r",", crontab_parameter)
    if len(splitting) == 5:
        searching_day_week = re.search(r'^[*|(1-7)]$', splitting[4])
        searching_month = re.search(r'^[*]|(\b([1-9]|1[0-2])\b)$', splitting[3])
        searching_day_month = re.search(r'^[*]|\b([1-9]|[12][0-9]|3[01])\b$', splitting[2])
        searching_hour = re.search(r'^[*]|\b([0-9]|[12][0-3])\b$', splitting[1])
        searching_minute = re.search(r'^[*]|\b([0-9]|[12][0-9]|3[0-9]|4[0-9]|5[0-9])\b', splitting[0])
        list_result = [searching_day_week, searching_month, searching_day_month, searching_hour, searching_minute]
        for i in list_result:
            if i != None:
                print("Valid parameters!")
            else:
                raise ValueError("Parameter not correct.")
    else:
        print("Please enter all parameters.")
