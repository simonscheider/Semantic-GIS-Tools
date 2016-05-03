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

  key = '' #This the OSM place category key
  value = '' #This the OSM place category value
  elem = ""
  tag_set = set()# this is the list of tags that come with the result set
  max_field_length = 0
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
        "public transport station": {"key" : "public_transport", "value" : "platform", "element" : "node"},
        "office": {"key" : "office", "value" : "", "element" : "node"},
        "leasure": {"key" : "leasure", "value" : "", "element" : "node"},
        "historic": {"key" : "historic", "value" : "", "element" : "node"},
        "civic building":  {"key" : "building", "value" : "civic", "element" : "area"},
        "school building":  {"key" : "building", "value" : "school", "element" : "area"},
        "building":  {"key" : "building", "value" : "", "element" : "area"},
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

  def createGeometry(self, element):
    if (self.elem == "node"):
         geom = arcpy.PointGeometry(arcpy.Point(float(element.lon), float(element.lat)),arcpy.SpatialReference(4326)).projectAs(self.rs)
    elif (self.elem == "area"):
         array = arcpy.Array()
         for n in element.get_nodes(resolve_missing=True):
            array.add(arcpy.Point(float(n.lon), float(n.lat)))
         geom = arcpy.Polygon(array,arcpy.SpatialReference(4326)).projectAs(self.rs)
    elif (self.elem == "line"):
         array = arcpy.Array()
         for n in element.get_nodes(resolve_missing=True):
            array.add(arcpy.Point(float(n.lon), float(n.lat)))
         geom = arcpy.Polyline(array,arcpy.SpatialReference(4326)).projectAs(self.rs)
    return geom

  def OSMtoShape(self, outFC):
         # Create the output feature class in WGS84
        #outFC = os.path.join(arcpy.env.workspace,arcpy.ValidateTableName("OSM"))
        if self.elem == "node":
            fc = 'POINT'
            res = self.result.nodes
        elif self.elem == "area":
            fc = 'POLYGON'
            res = self.result.ways
        elif self.elem == "line":
            fc = 'POLYLINE'
            res = self.result.ways

        arcpy.CreateFeatureclass_management(os.path.dirname(outFC), os.path.basename(outFC), fc, '', '', '', self.rs)

        # Join fields to the feature class, using ExtendTable


        tag_list = list(self.tag_set)
        tag_fields = map(lambda s: str(arcpy.ValidateFieldName(s)), tag_list)
        print tag_fields
        field_array = [('intfield', numpy.int32),
                        ('Name_d', '|S255'),
                        ('Value_d', '|S255'),
                        ('Key_d', '|S255'),
                        ]
        for f in tag_fields:
            field_array.append((f, '|S255'))
        print field_array
        inarray = numpy.array([],
                          numpy.dtype(field_array))

        arcpy.da.ExtendTable(outFC, "OID@", inarray, "intfield")

        field_list = ['Name_d', 'Value_d', 'Key_d', 'SHAPE@']
        field_list.extend(tag_fields)
        print field_list
        rowsDA = arcpy.da.InsertCursor(outFC, field_list)

        #arcpy.SetProgressor('step', 'Converting GPX points...', 0, howManyElements, 1)
        # Loop over each point in the tree and put the information inside a new row

        #Geometries and attributes are inserted
        for element in res:
            geom = self.createGeometry(element)
            f = lambda tag: element.tags.get(tag, "n/a")
            tag_values = map(f,tag_list)
            l = [element.tags.get("name", "n/a"), element.tags.get(self.key, "n/a"), self.key, geom]
            l.extend(tag_values)
            try:
              rowsDA.insertRow(l)
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
        #print cat
        #placeCategory = "amenity=police"

        pc = self.placeCategories[cat]
        if (pc["value"] == ""): #If querying only by key
            kv = pc["key"]
        else:
            kv = pc["key"]+"="+pc["value"]
        elem = pc["element"]

        if (elem =="area" or elem == "line"):
            OSMelem ="way"
        else:
            OSMelem ="node"

        bbox = ", ".join(self.listtoString(self.getCurrentBBinWGS84()))#"50.600, 7.100, 50.748, 7.157"

        #Using Overpass API: http://wiki.openstreetmap.org/wiki/Overpass_API
        result = api.query(OSMelem+"""("""+bbox+""") ["""+kv+"""];out body;
            """)
        results = []
        if (elem == "node"):
            results = result.nodes
        elif (elem == "area" or elem == "line"):
            results = result.ways

        print("Number of results:" + str(len(results)))
        self.max_field_length = 0
        for element in results:
            #print node.tags
           # print node.tags.
           #print element.id
           for tag in element.tags:
                #print(tag+": %s" % element.tags.get(tag, "n/a"))
                self.tag_set.add(tag)
                self.max_field_length= max(len(element.tags.get(tag, "n/a")),self.max_field_length)
##           if  (elem == "area" or elem == "line"):
##              for n in element.get_nodes(resolve_missing=True):
##                print("    Lat: %f, Lon: %f" % (n.lat, n.lon))
##           else:
##                print("    Lat: %f, Lon: %f" % (element.lat, element.lon))

        self.result = result
        self.elem = elem
        self.value = pc["value"]
        self.key = pc["key"]

def loadOSM(cat, tname):
    o = OSMLoad()
    print cat
    o.getOSMfeatures(cat)
    o.OSMtoShape(tname)

if __name__ == "__main__":
    cat = arcpy.GetParameterAsText(0)
    tname = arcpy.GetParameterAsText(1)
    #cat = "bar"
    #tname = r"C:\Users\simon\Documents\ArcGIS\Default.gdb\LoadOSM"
    loadOSM(cat, tname)