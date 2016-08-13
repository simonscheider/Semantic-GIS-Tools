# Typing gis:Erase
# Set inputs
# Set of region datasets as input and output
INSERT {
	?in a gis:Region.
	?er a gis:Region.
} WHERE{
	?node a gis:Erase;
			gis:inputdata ?in;
			gis:erasefeature ?er.
	FILTER NOT EXISTS { ?in a gis:Region.
						?er a gis:Region. } 
}
