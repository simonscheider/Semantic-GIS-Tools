# Typing gis:Intersect

#Set link
INSERT {
	?out2 ada:partof ?in2.
} WHERE {
	?node a gis:Intersect;
	 	gis:inputdata ?in;
		wf:output ?out.
	
	?in ada:hasElement ?in1.
	?in1 ada:hasAttribute ?in2.
	?in2 a gis:Region.
	
	?out ada:hasElement ?out1.
	?out1 ada:hasAttribute ?out2.
	?out2 a gis:Region.
}