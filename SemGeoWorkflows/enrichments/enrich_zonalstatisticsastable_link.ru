
# Typing gis:ZonalStatisticsAsTable

# TODO: propagate properties of zones?

# Set link
INSERT {
	?inm a ada:Quality.
	?outm a gis:QQuality;
		gis:ofprop ?inm.
	?out wf:of ?in.
	?ins ada:partOf ?outs.
	?zos owl:sameAs ?outs.
	?inm wf:of _:afield . _:afield a gis:SField. #Must be of a field
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		wf:output ?out;
		gis:inputraster ?in;
		gis:zones ?zo.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?zo ada:hasElement ?zoe. 
	?zoe ada:hasMeasure ?zom.
	?zoe ada:hasSupport ?zos.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
	
}
