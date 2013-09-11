# Homework assignment 1, part 2: Function
# Stephanie Kroese
# Due 9/12/2013
# This function will read burl1 data from the file 'burl1_1990.dat'
#   and put the SLP, wind components, and date/time into arrays. 
#   It will display (part of) these arrays

import numpy as np
from datetime import datetime

def readData1990():
    f = open('burl1_1990.dat')

    windCompNorth = []
    windCompEast = []
    pressure = []
    dates = []
    
    for line in f.readlines()[1:]:
        data=line.split()
        year = (int(data[0])+1900)
        month = int(data[1])
        day = int(data[2])
        hour = int(data[3])
        
        dates.append(datetime(year, month, day, hour))
        pressure.append(float(data[11]))
        windCompNorth.append((float(data[5]))*(np.cos(((float(data[4]))*3.14/180)+3.14)))
        windCompEast.append((float(data[5]))*(np.sin(((float(data[4]))*3.14/180)+3.14)))
                
    pressure = np.array(pressure)
    dates = np.array(dates)
    windCompNorth = np.array(windCompNorth)
    windCompEast = np.array(windCompEast)
      
    print 'Pressure (millibars): ', pressure
    print 'Northward wind components (knots): ', windCompNorth
    print 'Eastward wind components (knots): ', windCompEast
    print 'Date and time start at ', dates[0]
    print 'Date and time end at', dates[8718]

readData1990()

