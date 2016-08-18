# Typing gis:JoinField
# Set output structure
INSERT {
	?out a ada:DataSet;
		 ada:hasElement [
			ada:hasMeasure [ a ada:Quality ];
			ada:hasSupport _:outs
		  ].
} WHERE {
	?node a gis:JoinField;
		  wf:output ?out.
	FILTER NOT EXISTS { 
		?out ada:hasElement ?oute.
		?oute ada:hasMeasure ?outm.
		?oute ada:hasSupport ?outs.
	}
}
