# Typing gis:Erase

#Set link
INSERT {
	?out a gis:Region;
		 ada:partof ?in.
} WHERE{
	?node a gis:Erase;
			wf:output ?out;
			gis:inputdata ?in.
	FILTER NOT EXISTS { ?out a gis:Region;
							 ada:partof ?in. } 
}