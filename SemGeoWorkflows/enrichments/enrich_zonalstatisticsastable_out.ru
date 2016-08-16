
# Typing gis:ZonalStatisticsAsTable

#Set output
INSERT {
	?out a gis:ObjectDataSet; 
		ada:hasElement _:oute. 
	_:oute ada:hasMeasure _:outm.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		wf:output ?out.
	FILTER NOT EXISTS {
		?out ada:hasElement ?oute. 
		?oute ada:hasMeasure ?outm.
	}
}
