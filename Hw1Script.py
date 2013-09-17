# Homework assignment 1, part 1: Script
# Stephanie Kroese
# Due 9/17/2013
# This script will read burl1 data from the file 'burl1_2011.dat' and save the 
#     pressure, wind components, and date/time as arrays. It will then display 
#     these arrays.

import numpy as np
from datetime import datetime

f = open('burl1_2011.dat')

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
    minute = int(data[4])
    
    dates.append(datetime(year, month, day, hour, minute))
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
print 'Date and time begin at', dates[0]
print 'Date and time end at', dates[8759]



