

# Typing gis:LocalMapAlgebra


#Set output links
INSERT
{
?outm a gis:QQuality ; gis:ofprop ?inm .
?inm a ada:Quality.
} WHERE {
?node a gis:LocalMapAlgebra;
wf:output ?out;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. #Are data blank nodes present? Then reuse them
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.
}








