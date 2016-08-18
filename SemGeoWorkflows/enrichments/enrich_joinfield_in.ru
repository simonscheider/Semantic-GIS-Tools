# Typing gis:JoinField
# Set inputs
INSERT {
	?in a ada:DataSet;
		ada:hasElement [ 
			ada:hasMeasure [ a ada:Quality ];
			ada:hasSupport _:ins
		  ].
} WHERE {
	?node a gis:JoinField;
		  gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?ine.
		?ine ada:hasMeasure ?inm.
		?ine ada:hasSupport ?ins.
	}
}
