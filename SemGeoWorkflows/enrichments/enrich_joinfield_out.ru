# Typing gis:JoinField
# Set output structure
INSERT {
	?out a ada:DataSet;
		 ada:hasElement [ 
			ada:hasSupport [ a ada:Object ];
			ada:hasMeasure [ a ada:Quality ]
		  ].
} WHERE {
	?node a gis:JoinField;
		  wf:output ?out.
	FILTER NOT EXISTS { 
		?out ada:hasElement ?oute.
		?oute ada:hasAttribute ?outa.
	}
}
