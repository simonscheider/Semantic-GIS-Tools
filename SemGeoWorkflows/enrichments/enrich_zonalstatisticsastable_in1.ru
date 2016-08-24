
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in a gis:Raster.
		?ine ada:hasMeasure _:inm.		
	?zo a gis:SpatialDataSet.
		?zoe ada:hasMeasure _:zom.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputraster ?in;
		gis:zones ?zo.
		?in ada:hasElement ?ine.
		?zo ada:hasElement ?zoe.
	FILTER NOT EXISTS {		
		?ine ada:hasMeasure ?inm.		
		?zoe ada:hasMeasure ?zom.
	}
}
