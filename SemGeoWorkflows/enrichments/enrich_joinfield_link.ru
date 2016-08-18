# Typing gis:JoinField
# Set link
# Input and output have the same support.

# TODO: fix possible inference problems on sameAs

INSERT {
	?inm a ada:Quality.
	?outs owl:sameAs ?ins.
	?outm owl:sameAs ?inm.
} WHERE {
	?node a gis:JoinField;
		wf:output ?out;
		gis:inputdata ?in.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasSupport ?ins.
	?ine ada:hasMeasure ?inm.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasSupport ?outs.
	?oute ada:hasMeasure ?outm.
}