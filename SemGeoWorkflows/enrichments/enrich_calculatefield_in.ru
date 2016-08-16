
# Typing gis:CalculateField

#Set Input
INSERT {
	?in a ada:ObjectDataSet; 
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
