# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:22:13 2017

@author: PC

Expects a .dat type airfoil polar from airfoiltools.com
Converts airfoil plot into one the SolidWorks can use.
"""

def addZero(origin, newfile):
    """
        input: an open file handle to read from (origin).
        output: an open file handle to write into (newfile).
        
        Function turns spaces between each value in each line into tabs.
        Function then adds the value 0 for each line's Z axis.
    """
    n = 0
    tabFlag = False     #True if a tab was previously appended. Prevents multiple successive spaces being turned to multiple successive tabs.
    for line in origin:
        if n != 0:  #Does not add the first line, as it's usually the airfoil's name.
            str1 = ""   #Temporary string
            first = True
            for char in line:
                if char == "\n":    #If "carriage return", then:
                    str1 = str1 + "\t0\n"   #Then tabs, adds a zero, then ends line.
                    tabFlag = False
                elif char == " ":
                    if first == False:
                        if tabFlag == False:    #Prevents multiple successive tabs.
                            str1 = str1 + "\t"
                            tabFlag = True
                else:
                    str1 = str1 + char
                    tabFlag = False
                    first = False
            newfile.write(str1)
        n += 1
    
    
filename = input("File to convert?: " )
newfilename = input("New file name?: ")

try:
    origin = open(filename, "r")
    newfile = open(newfilename, "w")
except IOError:
    print("Couldn't open file or files, try again.")
else:
    addZero(origin, newfile)
    print("Conversion succeeded.")
finally:
    newfile.close()
    origin.close()
