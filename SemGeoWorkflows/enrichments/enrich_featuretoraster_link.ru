
# Typing gis:FeatureToRaster

#Set output
INSERT { 
	?out a gis:Raster. 
	?outm a gis:Existence; 
			wf:of ?in; 
			a gis:QQuality; 
			gis:ofprop ?inm. 
	?outs ada:partOf ?ins. # supports
	?inm wf:of _:gf; # field
		a ada:Quality.
	_:gf a gis:SField.
} WHERE {
	?node a gis:FeatureToRaster;
		wf:output ?out;
		gis:inputdata ?in2.
	?in2 ada:hasElement ?ine. 
	?ine gis:hasAttribute ?inm. ?inm a ada:Quality. # stay neutral with respect to measure or support
	?ine gis:hasAttribute ?ins. ?ins a gis:Region.
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
