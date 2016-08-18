
# Typing gis:FeatureToRaster

#Set Input
INSERT { 
	?ine gis:hasAttribute _:inm. # We stay here neutral as to whether measure or support
	_:inm a ada:Quality.
}WHERE{
	?node a gis:FeatureToRaster;
			gis:inputdata ?in2.
		?in2 ada:hasElement ?ine.
	FILTER NOT EXISTS{		 
		?ine gis:hasAttribute ?inm.
		?inm a ada:Quality.
	}
}
