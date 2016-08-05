#!/usr/bin/env python

"""
Tests of Semantic Workflows.

The script

1) loads RDF files in memory
2) runs semantic enrichments
2) runs tests
3) writes the final graph into a file

Based on RDFLib and RDFClosure (Python 2.7)
"""

__author__      = "Andrea Ballatore; Simon Scheider"
__copyright__   = ""

import os
import sys
from sys import argv
import rdflib
import RDFClosure
from rdflib.namespace import RDFS

def file_to_str(fn):
    with open(fn, 'r') as f:
        content=f.read().strip()
    return content
    
def n_triples( g, n=None ):
    if n is None:
        print( 'Triples: '+str(len(g)) )
    else:
        print( 'Triples: +'+str(len(g)-n) )

def run_rdfs_inferences( g ):
    print('run_rdfs_inferences')
    # expand deductive closure
    RDFClosure.DeductiveClosure(RDFClosure.RDFS_Semantics).expand(g)
    n_triples(g)
    return g
    
def load_ontologies( g ):
    print("load_ontologies")
    ontos = ["ontologies/Workflow.rdf","ontologies/GISConcepts.rdf","ontologies/AnalysisData.rdf"]
    for fn in ontos:
        print("Load RDF file: "+fn)
        g.parse( fn )
    n_triples(g)
    g = run_rdfs_inferences( g )
    return g
    
def enrich_workflow( g, toolname ):
    n = n_triples(g)
    assert toolname
    import glob
    inputs = glob.glob('enrichments/enrich_'+toolname+'_in*.ru')
    outputs = glob.glob('enrichments/enrich_'+toolname+'_out*.ru')
    for fn in (inputs + outputs):
        print('Enrichment '+fn)
        #g.update( file_to_str('prefixes_rdf.txt') + file_to_str(fn) )
        n_triples(g)
    return g
    
def test_workflow_lights( g ):
    print('> test_workflow_lights')
    _dir = "workflows/workflow_lights/"
    for fn in [_dir+"workflow_lights.ttl"]:
        print("Load N3 file: "+fn)
        g.parse( fn, format='n3' )
    #g = enrich_workflow( g, _dir )
    return g
    
def test_workflow_lcpath( g ):
    print('> test_workflow_lights')
    _dir = "workflows/workflow_lcpath/"
    for fn in [_dir+"workflow_lcpath.ttl"]:
        print("Load N3 file: "+fn)
        g.parse( fn, format='n3' )
    # TODO: run real enrichments
    g = enrich_workflow( g, 'polygontoraster' )
    return g
    
def graph_to_file( g ):
    _outfn = 'output/workflows_output.ttl'
    g.serialize( _outfn, 'n3' )
    print("Written triples to " + _outfn)

def main():
	# create inmemory store
    g = rdflib.ConjunctiveGraph()
    params = sys.argv[1:]
    
    g = load_ontologies( g )
    if 'lights' in params: g = test_workflow_lights( g )
    if 'lcpath' in params: g = test_workflow_lcpath( g )
    graph_to_file(g)
    print('OK')

if __name__ == '__main__':
    main()
