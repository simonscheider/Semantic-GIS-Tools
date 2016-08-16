
# Typing gis:ExtractByMask

#Set output structure
INSERT { 
	?out a gis:Raster;
		ada:hasElement [ ada:hasMeasure _:outm; ada:hasSupport _:outs ].
		
} WHERE {
	?node a gis:ExtractByMask;
			wf:output ?out.
	FILTER NOT EXISTS{
		?out ada:hasElement ?oute. 
		?oute ada:hasMeasure ?outm. 
		?oute ada:hasSupport ?outs. 
	}
}
