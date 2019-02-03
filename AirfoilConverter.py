# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:22:13 2017

@author: Ayberk Yaraneri

Expects a .dat type airfoil polar from airfoiltools.com
Converts airfoil plot into one that SolidWorks can use.
"""

def Convert(origin, newfile, scaleFactor):
    """
        input: an open file handle to read from (origin).
        output: an open file handle to write into (newfile).

        Function turns spaces between each value in each line into tabs.
        Function then adds the value 0 for each line's Z axis.
    """
    points = origin.read().split('\n')

    for point in points[1:]:
        coordinates = point.split()
        if len(coordinates):
            newfile.write(str.format('{0:.6f}', float(coordinates[0])*scaleFactor))
            newfile.write('\t')
            newfile.write(str.format('{0:.6f}', float(coordinates[1])*scaleFactor))
            newfile.write('\t')
            newfile.write('0.000000')
            newfile.write('\n')

filename = input("File to convert?: " )
scaleFactor = float(input("Scale?: "))
newfilename = input("New file name?: ")

try:
    origin = open(filename, "r")
    newfile = open(newfilename, "w")
except IOError:
    print("Couldn't open file or files, try again.")
else:
    Convert(origin, newfile, scaleFactor)
    print("Conversion succeeded.")
finally:
    newfile.close()
    origin.close()
