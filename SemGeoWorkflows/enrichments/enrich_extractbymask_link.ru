
# Typing gis:ExtractByMask

INSERT { 
	?outm gis:ofprop ?inm.
	?outs ada:partOf ?ins. 	# outcell is part of input raster cell
	 ?outs ada:partOf ?ms . 	# outcell is part of mask cell
} WHERE {
	?node a gis:ExtractByMask;
		wf:output ?out;
		gis:inputraster ?ras;
		gis:rastermask ?mask.
	
	?ras ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?mask ada:hasElement ?me. 
	?me ada:hasMeasure ?mm.
	?me ada:hasSupport ?ms.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
