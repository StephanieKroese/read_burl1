# Homework assignment 1, part 2: Function
# Stephanie Kroese
# Due 9/17/2013
# This function will read burl1 data from a burl1 file and put the pressure, 
#     wind components, and date/time into arrays. It will then display these 
#     arrays.
# Note: I noticed that some of the earlier burl1 files had a slightly different
#     format for the data. Using this function on an earlier data set may result
#     in an error (I tried it on the burl1_1990 data and an error occured).

import numpy as np
from datetime import datetime

def readData(fileName1):
    f = open(fileName1)

    windCompNorth = []
    windCompEast = []
    pressure = []
    dates = []
    
    for line in f.readlines()[2:]:
        data=line.split()
        year = int(data[0])
        month = int(data[1])
        day = int(data[2])
        hour = int(data[3])
        minutes = int (data[4])
        
        dates.append(datetime(year, month, day, hour, minutes))
        pressure.append(float(data[12]))
        windCompNorth.append((float(data[6]))*np.cos((float(data[5]))*3.14/180))
        windCompEast.append(-(float(data[6]))*np.sin((float(data[5]))*3.14/180))
                
    pressure = np.array(pressure)
    dates = np.array(dates)
    windCompNorth = np.array(windCompNorth)
    windCompEast = np.array(windCompEast)
      
    print 'Pressure (millibars): ', pressure
    print 'Northward wind components (m/s): ', windCompNorth
    print 'Eastward wind components (m/s): ', windCompEast
    print 'Date and time start at ', dates[0]
    print 'Date and time end at', dates[8759]

readData('burl1_2011.dat')

