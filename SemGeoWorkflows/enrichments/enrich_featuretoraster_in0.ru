
# Typing gis:FeatureToRaster

#Set Input
INSERT { 
	?in2 ada:hasElement _:ine. 	
}WHERE{
	?node a gis:FeatureToRaster;
			gis:inputdata ?in2.
	FILTER NOT EXISTS{
		?in2 ada:hasElement ?ine. 		
	}
}
