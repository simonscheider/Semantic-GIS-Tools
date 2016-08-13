# Typing gis:Buffer

# The output of the Buffer is a set of neighborhoods of input objects
INSERT {
	?at2 wf:of ?at.
} WHERE {
	?node a gis:Buffer;
		gis:inputdata ?in;	
		wf:output ?out.
	
	?in ada:hasElement ?inel.
	?inel ada:hasSupport ?at.
	?at a ada:Object.
	
	?out ada:hasElement ?outel.
	?outel ada:hasSupport ?at2.
	?at2 a gis:Neighborhood.
}