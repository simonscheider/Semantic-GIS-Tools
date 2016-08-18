
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in a gis:Raster;
		ada:hasElement _:ine.
	_:ine ada:hasSupport _:ins.
	?zo a gis:ObjectDataSet;
		ada:hasElement _:zoe.
	_:zoe ada:hasSupport _:zos.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputraster ?in;
		gis:zones ?zo.
		?in ada:hasElement ?ine.
		?zo ada:hasElement ?zoe.
	FILTER NOT EXISTS {		
		?ine ada:hasSupport ?inm.		
		?zoe ada:hasSupport ?zom.
	}
}
