# Typing gis:Intersect

#Set link
INSERT {
	?out2 ada:partOf ?in2.
} WHERE {
	?node a gis:Intersect;
	 	gis:inputdata ?in;
		wf:output ?out.
	
	?in ada:hasElement ?in1.
	?in1 gis:hasAttribute ?in2.
	?in2 a gis:Region.
	
	?out ada:hasElement ?out1.
	?out1 gis:hasAttribute ?out2.
	?out2 a gis:Region.
}