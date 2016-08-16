
# Typing gis:ExtractByMask

#Set output
INSERT { 
	?outm wf:of ?in;
		gis:ofprop ?inm.
	?outs ada:partof ?ins.
} WHERE {
	?node a gis:ExtractByMask;
		wf:output ?out;
		gis:inputdata ?in2.
	
	?in2 ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
