# Typing gis:Buffer
# Set inputs
# Set of region datasets as input
INSERT {
	?in a ada:DataSet;
		ada:hasElement [
			ada:hasSupport [ a ada:Object ]; 
			ada:hasMeasure [ a ada:Spatial ]
		].
} WHERE{
	?node a gis:Buffer;
		gis:inputdata ?in.
	FILTER NOT EXISTS { 
		?in ada:hasElement ?in1.
		?in1 ada:hasSupport ?in2.
		?in2 a ada:Object.
		
		?ina ada:hasElement ?ina1.
		?ina1 ada:hasMeasure ?ina2.
		?ina2 a ada:Spatial.
	}
}
