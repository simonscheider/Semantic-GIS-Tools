
# Typing gis:CalculateField

# TODO: gis:ObjectDataSet might be too restrictive

# Set output structure
INSERT { 
	?out a gis:SpatialDataSet;
		ada:hasElement [ 
			ada:hasMeasure _:outm; 
			ada:hasSupport _:outs
		].
} WHERE {
	?node a gis:CalculateField;
			wf:output ?out.
	FILTER NOT EXISTS{
		?out ada:hasElement ?oute. 
		?oute ada:hasMeasure ?outm. 
		?oute ada:hasSupport ?outs. 
	}
}
