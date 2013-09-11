# Homework assignment 1, part 3: Class
# Stephanie Kroese
# Due 9/12/2013
# This contains a class that will return an instance of the burl1_1990 data.
# It will print the first five values of the SLP and wind components, as well 
#     as the date and time of the beginning and end of the data

import numpy as np
from datetime import datetime
from math import cos
from math import sin

class burlData():
    
    def __init__(self, fileName1):
        self.fileName1 = fileName1
        
    def windCompNorth(self, number):
        data1=open('burl1_1990.dat')
        windCompNorth=[]
        for line in data1.readlines()[1:]:
            data=line.split()
            windspeed = float(data[5])
            windDir = (((float(data[4]))+180)*(3.14/180))
            windCompNorth.append(windspeed*(cos(windDir)))
        windCompNorth=np.array(windCompNorth)
        print windCompNorth[0:number]
        
    def windCompEast(self, number):
        data1=open('burl1_1990.dat')
        windCompEast=[]
        for line in data1.readlines()[1:]:
            data=line.split()
            windspeed = float(data[5])
            windDir = (((float(data[4]))+180)*(3.14/180))
            windCompEast.append(windspeed*(sin(windDir)))
        windCompEast=np.array(windCompEast)
        print windCompEast[0:number]
        
    def pressure(self, number):
        data1=open('burl1_1990.dat')
        pressure=[]
        for line in data1.readlines()[1:]:
            data=line.split()
            pressure.append(float(data[11]))
        pressure=np.array(pressure)
        print pressure[0:number]
        
    def dateAndTime(self, number):
        data1=open('burl1_1990.dat')
        dateAndTime=[]
        for line in data1.readlines()[1:]:
            data=line.split()
            year = int(data [0])+1900
            month = int(data [1])
            day = int(data [2])
            hour = int(data [3])
            dateAndTime.append(datetime(year, month, day, hour))
        print dateAndTime[number]
        

attempt1=burlData('burl1_1990.dat')

print 'Northerly wind components (first five in array):'
attempt1.windCompNorth(5)
print '\nEasterly wind components (first five in array):'
attempt1.windCompEast(5)
print '\nSea Level Pressure (first five in array): '
attempt1.pressure(5)
print '\nBeginning date and time:'
attempt1.dateAndTime(0)
print '\nEnding date and time:'
attempt1.dateAndTime(8718)