
import arcpy

def checkUniquness(table, field):
     sett = set()
     number = 0
     cursor = arcpy.da.SearchCursor(table, [field])
     for row in cursor:
        sett.add(row[0])
        number+=1
     del row
     del cursor
     print 'Size of value set: '+str(len(sett))
     print 'Size of value list: '+str(number)
     return len(sett)==number


def updateTableC(table, field):
    #updates the given column (field) of a given table by filling in unique numbers starting from 1
    number = 0
    cursor = arcpy.da.UpdateCursor(table, [field])
    for row in cursor:
        number = number + 1
        row[0] = number
        cursor.updateRow(row)
    del row
    del cursor

#updateTableC()


table = 'Roads16'
field = 'BN2000_'
print "Test: is the field unique? "+str(checkUniquness(table, field))
#updateTableC(table, field)

