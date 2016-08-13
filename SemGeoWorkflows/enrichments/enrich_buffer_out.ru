# Typing gis:Buffer

INSERT {
	?out a ada:DataSet;
		ada:hasElement [ 
			ada:hasSupport [ a gis:Neighborhood ];
			ada:hasMeasure [ a gis:Region ]
		].
} WHERE{
	?node a gis:Buffer;
			wf:output ?out.
	FILTER NOT EXISTS { 
		?out ada:hasElement ?out1.
		?out1 ada:hasSupport ?out2.
		?out2 a gis:Neighborhood.
		?out1 ada:hasMeasure ?outa2.
		?outa2 a gis:Region.
	} 
}