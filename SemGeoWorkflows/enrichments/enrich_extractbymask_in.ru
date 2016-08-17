
# Typing gis:ExtractByMask

#Set Input
INSERT { 
	?in a gis:Raster;
		ada:hasElement _:ine. 
	_:ine ada:hasSupport _:ins. 
	_:ins a gis:Region.
} WHERE {
	?node a gis:ExtractByMask;
		gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?ine.
		?ine ada:hasSupport ?ins.
		?ins a ada:Object.
		
		?ina ada:hasElement ?ina1.
		?ina1 ada:hasMeasure ?ina2.
		?ina2 a ada:Spatial.
	}
}
