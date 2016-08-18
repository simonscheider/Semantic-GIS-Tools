
# Typing gis:ZonalStatisticsAsTable

# TODO: propagate properties of zones?

# Set link
INSERT {
	?inm a ada:Quality.
	?outm a gis:QQuality;
		gis:ofprop ?inm.
	?out wf:of ?in.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		wf:output ?out;
		gis:inputraster ?in;
		gis:zones ?zo.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	
	?zo ada:hasElement ?zoe. 
	?zoe ada:hasMeasure ?zom.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
}
