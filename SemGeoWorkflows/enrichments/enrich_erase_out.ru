# Typing gis:Erase

# Set of region datasets
INSERT {
	?out a gis:Region.
} WHERE{
	?node a gis:Erase;
			wf:output ?out.
	FILTER NOT EXISTS { ?out a gis:Region. } 
}