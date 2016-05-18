#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     13-05-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
count = 0
activated = []
finished = []
with open('C:\\Research\\UU\\Lehre\\AdvancedGIS\\ESRIcodes\\status.csv', 'rb') as f:
    reader = csv.reader(f, delimiter= ";")
    for row in reader:
        if (row[0] == 'Learning ArcGIS Desktop (for ArcGIS 10.0)' and row[2]=="simonscheider@web.de"):


            if (not (row[1]).__contains__("Code not activated") and row[6]==""):
                activated.append([row[1],row[3],row[4],row[5],row[6]])
                print row
                count = count+1
            elif (not (row[1]).__contains__("Code not activated") and row[6]!=""):
                finished.append([row[1],row[3],row[4],row[5],row[6]])
                print row
                count = count+1
print count
print len(activated)
print len(finished)

def main():
    pass

if __name__ == '__main__':
    main()
