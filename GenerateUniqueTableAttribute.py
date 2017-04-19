
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
        cursor.updateRow([row])
    del row
    del cursor

#updateTableC()

if __name__ == '__main__':
    #arcpy.env.workspace ='C:\Users\simon\Documents\GitHub\ArcGIS-Tools\TestingStuff'
    table = 'Roads_2001'
    field = 'BN2000_'
    print str(checkUniquness(table, field))


##print arcpy.CheckExtension("spatial")
##arcpy.env.workspace = "C:\Temp\AdvancedGIS"
##print arcpy.Describe("endraster").dataType
##print arcpy.Exists("my_roads_merge.shp")