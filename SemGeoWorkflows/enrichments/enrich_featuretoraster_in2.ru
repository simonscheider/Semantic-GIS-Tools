
# Typing gis:FeatureToRaster

#Set Input
INSERT {
	?ine ada:hasSupport _:inr.
	_:inr a gis:Region.
	?in a gis:RegionDataSet.
} WHERE {
	?node a gis:FeatureToRaster;
		gis:inputdata ?in.
	?in ada:hasElement ?ine.
	FILTER NOT EXISTS {
		?ine ada:hasSupport ?ins.
		?ins a gis:Region.
	}
}
