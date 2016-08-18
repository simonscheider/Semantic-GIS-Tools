# Typing gis:Intersect
# Set inputs
INSERT {
	?in ada:hasElement [ gis:hasAttribute [ a gis:Region ] ].
} WHERE {
	?node a gis:Intersect;
		  gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?in1.
		?in1 gis:hasAttribute ?in2.
		?in2 a gis:Region.
	}
}
