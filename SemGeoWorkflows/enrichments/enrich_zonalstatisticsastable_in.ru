
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in2 a gis:Raster;
		ada:hasElement _:ine.
	_:ine ada:hasMeasure _:inm.
	?zo a gis:ObjectDataSet;
		ada:hasElement _:zoe.
	_:zoe ada:hasMeasure _:zom.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputdata ?in2;
		gis:zones ?zo.
	FILTER NOT EXISTS {
		?in2 ada:hasElement ?ine. 
		?ine ada:hasMeasure ?inm.
	}
}
