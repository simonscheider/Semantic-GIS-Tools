#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     04-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import overpy
import arcpy
import os
import numpy
#import easygui

class OSMLoad(object):
  ''' Object to get OSM data '''

  pc = '' #This the OSM place category
  result = '' #This the result object
  rs = '' #This the reference system object of the current mapview
  placeCategories = {#this is a dictionary of place categories in OSM based on they key value pairs.
  #Possible categories can be retrieved at:
        "amenity": 	{"key" : "amenity","value" : "", "element" : "node"},
        "shop": 	{"key" : "shop","value" : "", "element" : "node"},
        "bar": {"key" : "amenity", "value" : "bar", "element" : "node"},
        "police": {"key" : "amenity", "value" : "police", "element" : "node"},
        "optician": {"key" : "shop", "value" : "optician", "element" : "node"},
        "station": {"key" : "railway", "value" : "station", "element" : "node"},
        "ptstation": {"key" : "public_transport", "value" : "platform", "element" : "node"},
        "office": {"key" : "office", "value" : "", "element" : "node"},
        "leasure": {"key" : "leasure", "value" : "", "element" : "node"},
        "historic": {"key" : "historic", "value" : "", "element" : "node"},
        }
  placeList = sorted(placeCategories.keys())
  base = ""
  path = ""

  def listtoString(self,list):
        l = []
        for s in list:
            l.append(str(s))
        return l

    # Gets the extent of the current map view in WGS84
  def getCurrentBBinWGS84(self):
        cmapdoc = arcpy.mapping.MapDocument("CURRENT")
        cdf = arcpy.mapping.ListDataFrames(cmapdoc, "Layers")[0]
        extentPolygon = arcpy.Polygon(arcpy.Array([cdf.extent.lowerLeft,cdf.extent.lowerRight, cdf.extent.upperRight, cdf.extent.upperLeft]), cdf.spatialReference)
        self.rs = cdf.spatialReference
        extentPolygoninWGS84 = extentPolygon.projectAs("WGS 1984") #arcpy.SpatialReference(4326)
        ex = extentPolygoninWGS84.extent
        return [ex.YMin,ex.XMin,ex.YMax,ex.XMax]
        del cmapdoc

    #print getCurentBBinWGS84()


  def genPath(self):
        self.path = str(arcpy.env.workspace)
        self.base = arcpy.ValidateTableName("OSM")
#        if (arcpy.Exists(outFC)):
#            d = arcpy.Describe(outFC)
#            path = d.path
#            base = d.basename
#        else:
        outFC = os.path.join(self.path,self.base)
        nr = 0
        #if (outFC == path):
        #    path = os.path.dirname(path)
        while (arcpy.Exists(outFC)):
            self.base = self.base+str(nr+1)
            outFC = os.path.join(self.path,self.base)
        return outFC

  def OSMtoShape(self, outFC):
         # Create the output feature class in WGS84
        #outFC = os.path.join(arcpy.env.workspace,arcpy.ValidateTableName("OSM"))
        arcpy.CreateFeatureclass_management(os.path.dirname(outFC), os.path.basename(outFC), 'POINT', '', '', '', self.rs)

        # Join fields to the feature class, using ExtendTable
        inarray = numpy.array([],
                          numpy.dtype([('intfield', numpy.int32),
                                       ('Name', '|S255'),
                                       ('Value', '|S' + str(len(str(self.pc[0])))),
                                       ('Key', '|S' + str(len(str(self.pc[1])))),
                                       ]))

        arcpy.da.ExtendTable(outFC, "OID@", inarray, "intfield")


        rowsDA = arcpy.da.InsertCursor(outFC, ['Name', 'Value', 'Key', 'SHAPE@'])

        #arcpy.SetProgressor('step', 'Converting GPX points...', 0, howManyElements, 1)
        # Loop over each point in the tree and put the information inside a new row

        #Currently only nodes are explored
        c = 0
        for node in self.result.nodes:
            point = arcpy.PointGeometry(arcpy.Point(float(node.lon), float(node.lat)),arcpy.SpatialReference(4326)).projectAs(self.rs)
            try:
              rowsDA.insertRow([node.tags.get("name", "n/a"), str(self.pc[0]), str(self.pc[1]),  point])
              c=+1
            except RuntimeError, e:
              arcpy.AddError(str(e))

            #arcpy.SetProgressorPosition(c)
        if rowsDA:
            del rowsDA

##        mxd = arcpy.mapping.MapDocument("CURRENT")
##        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
##        arcpy.mapping.AddLayer(df, addLayer, "AUTO_ARRANGE")
##        arcpy.RefreshActiveView()
##        arcpy.RefreshTOC()
        # create layer in TOC and reference it in a variable for possible other actions
##        newLyr = arcpy.MakeFeatureLayer_management(
##            outFC,
##            "OSM_lyr"
##        )#    arcpy.RefreshActiveView()
        #arcpy.RefreshTOC()

  def getOSMfeatures(self, cat):
        api = overpy.Overpass()
        print cat
        #placeCategory = "amenity=police"

        pc = self.placeCategories[cat]
        if (pc["value"] == ""): #If querying only by key
            kv = pc["key"]
        else:
            kv = pc["key"]+"="+pc["value"]
        elem = pc["element"]

        bbox = ", ".join(self.listtoString(self.getCurrentBBinWGS84()))#"50.600, 7.100, 50.748, 7.157"

        #Using Overpass API: http://wiki.openstreetmap.org/wiki/Overpass_API
        result = api.query(elem+"""("""+bbox+""") ["""+kv+"""];out body;
            """)
        results = []
        if (elem == "node"):
            results = result.nodes
        elif (elem == "way"):
            results = result.ways

        print("Number of results:" + str(len(results)))
        for node in results:
            #print node.tags
           # print node.tags.
           for tag in node.tags:
              #  print(tag)
                print(tag+": %s" % node.tags.get(tag, "n/a"))
           print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
        self.result = result
        self.pc = [pc["value"],pc["key"]]

def loadOSM(cat, tname):
    o = OSMLoad()
    print cat
    o.getOSMfeatures(cat)
    o.OSMtoShape(tname)

if __name__ == "__main__":
    cat = arcpy.GetParameterAsText(0)
    tname = arcpy.GetParameterAsText(1)
    loadOSM(cat, tname)