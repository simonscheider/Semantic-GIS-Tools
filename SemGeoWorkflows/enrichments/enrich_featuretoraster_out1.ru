
# Typing gis:FeatureToRaster

#Set output structure
INSERT { 
	?out ada:hasElement [ ada:hasMeasure _:outm; ada:hasSupport _:outs ]. 
} WHERE {
	?node a gis:FeatureToRaster;
			wf:output ?out.
	FILTER NOT EXISTS{
		?out ada:hasElement ?oute. 
		?oute ada:hasMeasure ?outm. 
		?oute ada:hasSupport ?outs. 
	}
}
