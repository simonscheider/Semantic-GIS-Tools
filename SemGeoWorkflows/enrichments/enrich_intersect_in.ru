# Typing gis:Intersect
# Set inputs
INSERT {
	?in ada:hasElement [ ada:hasAttribute [ a gis:Region ] ].
} WHERE {
	?node a gis:Intersect;
		  gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?in1.
		?in1 ada:hasAttribute ?in2.
		?in2 a gis:Region.
	}
}
