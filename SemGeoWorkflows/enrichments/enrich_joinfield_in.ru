# Typing gis:JoinField
# Set inputs
INSERT {
	?in a ada:DataSet;
		 ada:hasElement [ 
			ada:hasSupport [ a ada:Object ];
			ada:hasMeasurement [ a ada:Quality ]
		  ].
} WHERE {
	?node a gis:JoinField;
		  gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?in1.
		?in1 ada:hasAttribute ?in2.
	}
}
