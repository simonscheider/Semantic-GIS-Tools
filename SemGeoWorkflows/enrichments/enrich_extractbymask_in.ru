
# Typing gis:ExtractByMask

#Set Input
INSERT { 
	?in a gis:Raster.
} WHERE {
	?node a gis:ExtractByMask;
		gis:inputdata ?in.
}
