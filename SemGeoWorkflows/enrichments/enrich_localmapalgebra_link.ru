
# Typing gis:LocalMapAlgebra

#Set output links
INSERT {
	?outm a gis:QQuality; 
		gis:ofprop ?inm.
	?inm a ada:Quality.
	?ins owl:sameAs ?outs. # supports are the same
} WHERE {
	?node a gis:LocalMapAlgebra;
		wf:output ?out;
		gis:inputdata ?in2.
	
	?in2 ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
