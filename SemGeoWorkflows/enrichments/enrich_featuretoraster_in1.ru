
# Typing gis:FeatureToRaster

#Set Input
INSERT 
{ 
	?in2 ada:hasElement _:ine. 
	_:ine ada:hasMeasure _:inm. 
	_:inm a ada:Quality.
}
WHERE{
	?node a gis:FeatureToRaster;
			gis:inputdata ?in2.
	FILTER NOT EXISTS{
		?in2 ada:hasElement ?ine. 
		?ine ada:hasMeasure ?inm.
	}
}
