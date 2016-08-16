
# Typing gis:FeatureToRaster

#Set output
INSERT { 
	?out a gis:Raster. 
	?outm a gis:Existence; 
			wf:of ?in; 
			a gis:QQuality; 
			gis:ofprop ?inm. 
	?outs ada:partof ?ins.
	?inm wf:of _:gf.
	?inm a ada:Quality.
	_:gf a gis:SField.
} WHERE {
	?node a gis:FeatureToRaster;
			wf:output ?out;
	gis:inputdata ?in2.
	?in2 ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
