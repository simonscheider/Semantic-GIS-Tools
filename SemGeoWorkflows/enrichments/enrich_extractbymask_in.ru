
# Typing gis:ExtractByMask

#Set Input
INSERT {
	?in a gis:Raster;
		ada:hasElement _:ine.
	_:ine ada:hasSupport _:ins.
	_:ins a gis:Region.
	_:ine ada:hasMeasure _:inm.
} WHERE {
	?node a gis:ExtractByMask;
		gis:inputraster ?in.
	FILTER NOT EXISTS {
		?in ada:hasElement ?ine.
		?ine ada:hasSupport ?ins.
		
		?ina ada:hasElement ?ina1.
		?ina1 ada:hasMeasure ?ina2.
	}
}
