

# Typing gis:LocalMapAlgebra


#Set output structure
INSERT {
	?out a gis:Raster; 
	  	ada:hasElement _:oute.
	_:oute ada:hasMeasure _:outm.
	_:oute ada:hasSupport _:outs.
} WHERE {
	?node a gis:LocalMapAlgebra;
		wf:output ?out.
	FILTER NOT EXISTS {
		?out ada:hasElement ?oute.
		?oute ada:hasMeasure ?outm.
		?oute ada:hasSupport ?outs.
	}
}

