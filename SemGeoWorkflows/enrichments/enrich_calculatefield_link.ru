
# Typing gis:CalculateField

#Set output
INSERT { 
	?inm a ada:Quality.
	?outm a gis:QQuality;
		gis:ofprop ?inm.
	?out wf:of ?in.
} WHERE {
	?node a gis:CalculateField;
		wf:output ?out;
		gis:inputdata ?in2.
	
	?in2 ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
