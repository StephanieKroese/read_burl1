# Homework assignment 1, part 3: Class
# Stephanie Kroese
# Due 9/17/2013
# This script will create a class for the burl1 data. It will store the pressure,
#     dates and times, and wind components of the data. It will then display this
#     information


import numpy as np
from datetime import datetime

class burlData():
    ''' This contains a class that will return an instance of burl1 data.
    It will print the first five values of the SLP and wind components, as well
    as the date and time of the beginning and end of the data. Note that not 
    all years of burl data will have the same columns in the data files, so using 
    this class for older burl data sets may result in an error.
    '''
    
    def __init__(self, fileName1):
        self.fileName1 = fileName1
        f=open(self.fileName1)
        
        dateAndTime=[]
        pressure = []
        NorthWindComp = []
        EastWindComp = []
        
        for line in f.readlines()[2:]:
            data=line.split()
            year = int(data [0])
            month = int(data [1])
            day = int(data [2])
            hour = int(data [3])
            minute = int(data[4])
            
            dateAndTime.append(datetime(year, month, day, hour, minute))
            pressure.append(float(data[12]))
            NorthWindComp.append((float(data[6]))*np.cos((float(data[5]))*3.14/180))
            EastWindComp.append(-(float(data[6]))*np.sin((float(data[5]))*3.14/180))
            
        dateAndTime=np.array(dateAndTime)
        pressure=np.array(pressure)
        NorthWindComp=np.array(NorthWindComp)
        EastWindComp=np.array(EastWindComp)
        
        self.dateAndTime=dateAndTime
        self.pressure=pressure
        self.NorthWindComp=NorthWindComp
        self.EastWindComp=EastWindComp
        
        
burl1_2011_info=burlData('burl1_2011.dat')

print 'Northerly wind components are: ', burl1_2011_info.NorthWindComp, ' meters per second'
print 'Easterly wind components are: ', burl1_2011_info.EastWindComp, ' meters per second'
print 'Pressures are: ', burl1_2011_info.pressure, ' millibars '
print 'Dates and times are: ', burl1_2011_info.dateAndTime[1], ' through ', burl1_2011_info.dateAndTime[8759]