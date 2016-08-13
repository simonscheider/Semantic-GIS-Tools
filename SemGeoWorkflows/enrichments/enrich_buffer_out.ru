# Typing gis:Buffer

INSERT {
	?out a ada:DataSet;
		ada:hasElement [ 
			ada:hasSupport _:sup;
			ada:hasMeasure _:mea
		].
	_:sup a gis:Neighborhood.
	_:mea a gis:Region.
	# region is of an object
	_:mea wf:of _:sup .
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