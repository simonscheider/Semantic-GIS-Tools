# Typing gis:JoinField
# Set output structure
#Set link
INSERT {
	?inm a ada:Quality.
	?out ada:partof ?in.
} WHERE {
	?node a gis:JoinField;
		wf:output ?out;
		gis:inputdata ?in.
	
	?in ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
}
