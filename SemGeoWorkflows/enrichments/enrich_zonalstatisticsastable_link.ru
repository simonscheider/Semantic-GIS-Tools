
# Typing gis:ZonalStatisticsAsTable

#Set link
INSERT {
	?inm a ada:Quality.
	?outm a gis:QQuality; 
		gis:ofprop ?inm.
	?out wf:of ?in.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		wf:output ?out;
		gis:inputdata ?in.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
}
