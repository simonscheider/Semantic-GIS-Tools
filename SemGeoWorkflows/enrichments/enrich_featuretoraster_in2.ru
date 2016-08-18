
# Typing gis:FeatureToRaster

#Set Input
INSERT {
	?ine gis:hasAttribute _:inr.
	_:inr a gis:Region.
	?in a gis:RegionDataSet.
} WHERE {
	?node a gis:FeatureToRaster;
		gis:inputdata ?in.
	?in ada:hasElement ?ine.
	FILTER NOT EXISTS {
		?ine gis:hasAttribute ?ins.
		?ins a gis:Region.
	}
}
