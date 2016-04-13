
import arcpy


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


print arcpy.CheckExtension("spatial")
arcpy.env.workspace = "C:\Temp\AdvancedGIS"
print arcpy.Describe("endraster").dataType
print arcpy.Exists("my_roads_merge.shp")