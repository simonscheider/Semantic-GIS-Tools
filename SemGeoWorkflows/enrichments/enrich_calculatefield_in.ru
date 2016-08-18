
# Typing gis:CalculateField

# TODO: no effect on #ZonalSt_shp1_1, but this seems correct.

#Set Input
INSERT {
	?in a gis:ObjectDataSet; 
		ada:hasElement _:ine. 
	_:ine ada:hasMeasure _:inm.
} WHERE {
	?node a gis:CalculateField;
		gis:inputdata ?in.
	FILTER NOT EXISTS{
		?in ada:hasElement ?ine. 
		?ine ada:hasMeasure ?inm.
	}
}
