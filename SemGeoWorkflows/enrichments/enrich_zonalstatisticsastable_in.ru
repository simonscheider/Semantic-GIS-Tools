
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in a gis:Raster;
		ada:hasElement _:ine.
	_:ine ada:hasMeasure _:inm.
	?zo a gis:ObjectDataSet;
		ada:hasElement _:zoe.
	_:zoe ada:hasMeasure _:zom.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputraster ?in;
		gis:zones ?zo.
	FILTER NOT EXISTS {
		?in ada:hasElement ?ine.
		?ine ada:hasMeasure ?inm.
		?zo ada:hasElement ?zoe.
		?zoe ada:hasMeasure ?zom.
	}
}
