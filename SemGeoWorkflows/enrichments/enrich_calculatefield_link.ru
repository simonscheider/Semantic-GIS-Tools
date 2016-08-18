
# Typing gis:CalculateField

#Set link
INSERT {
	?inm a ada:Quality.
	?outm a gis:QQuality;
		gis:ofprop ?inm.
	?out wf:of ?in.
} WHERE {
	?node a gis:CalculateField;
		wf:output ?out;
		gis:inputdata ?in.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
