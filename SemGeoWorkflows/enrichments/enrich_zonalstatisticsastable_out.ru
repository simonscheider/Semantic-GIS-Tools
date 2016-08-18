
# Typing gis:ZonalStatisticsAsTable

#Set output
INSERT {
	?out a gis:ObjectDataSet; 
		ada:hasElement _:oute.
	_:oute ada:hasMeasure _:outm.
	_:oute ada:hasSupport _:outs.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		wf:output ?out.
	FILTER NOT EXISTS {
		?out ada:hasElement ?oute. 
		?oute ada:hasMeasure ?outm.
		?oute ada:hasSupport ?outs.
	}
}
