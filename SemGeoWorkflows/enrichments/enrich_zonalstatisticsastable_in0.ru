
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in a gis:Raster;
		ada:hasElement _:ine.	
	?zo a gis:SpatialDataSet;#a gis:ObjectDataSet; This is too restrictive I think
		ada:hasElement _:zoe.	
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputraster ?in;
		gis:zones ?zo.
	FILTER NOT EXISTS {
		?in ada:hasElement ?ine.		
		?zo ada:hasElement ?zoe.
		
	}
}
