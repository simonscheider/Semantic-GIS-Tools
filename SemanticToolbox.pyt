import arcpy
import OSMLoad
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Semantic toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [LoadOSM]


class LoadOSM(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Load OSM"
        self.description = "Reads fresh OSM data from the OSM API into the current map view"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        cat = arcpy.Parameter(
            displayName="OSM categories",
            name="cat",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        #cat.columns = [['String', 'OSM categories']
        o = OSMLoad.OSMLoad()
        cat.filter.type = 'ValueList'
        cat.filter.list = o.placeCategories.keys().sort()

        outfeatures = arcpy.Parameter(
            displayName="Output Feature Class",
            name="outfeatures",
            datatype = "GPFeatureLayer",
            parameterType="Required",
            direction="Output")
        outfeatures.filter.list = ["Point"]
        #outfeatures.value = o.genPath()

        params = [cat, outfeatures]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
##        if (parameters[1].value==None):
##          parameters[1].value = os.path.join(arcpy.env.workspace,arcpy.ValidateTableName("OSM"))
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        OSMLoad.loadOSM(parameters[0], parameters[1])
        return
