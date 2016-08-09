#!/usr/bin/env python

"""
Tests of Semantic Workflows.

The script

1) loads RDF files in memory
2) runs semantic enrichments
2) runs tests
3) writes the final graph into a file



Based on Python 2.7 with:

* RDFLib (# pip install rdflib)
* RDFClosure (install manually from https://github.com/RDFLib/OWL-RL)

"""

__author__      = "Andrea Ballatore; Simon Scheider"
__copyright__   = ""

import os
import sys
from sys import argv
import rdflib
import RDFClosure
from rdflib.namespace import RDFS, RDF

class tools():
    toolenrichments = []
    tests =[]
    def __str__(self):
        return str(toolenrichments)

def file_to_str(fn):
    """ 
    Loads the content of a text file into a string
    @return a string
    """
    with open(fn, 'r') as f:
        content=f.read().strip()
    return content

def n_triples( g, n=None ):
    """ Prints the number of triples in graph g """
    if n is None:
        print( 'Triples: '+str(len(g)) )
    else:
        print( 'Triples: +'+str(len(g)-n) )
    return len(g)

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
    return g

def enrich_workflow_tool( g, toolname, tool):
    n = n_triples(g)
    assert toolname
    import glob
    inputs = glob.glob('enrichments/enrich_'+toolname+'_in*.ru')
    outputs = glob.glob('enrichments/enrich_'+toolname+'_out*.ru')
    tests =glob.glob('enrichments/enrich_'+toolname+'_test*.ru')
    growin = 0
    growout = 0
    for fn in (inputs):
        print('Enrichment '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        growin +=len(g)-n
        n= n_triples(g)
    for fn in (outputs):
        print('Enrichment '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        growout =len(g)-n
        n= n_triples(g)
    test = None
    for i in tests:
        print('Run test '+i)
        res = g.query(file_to_str('rdf_prefixes.txt') + file_to_str(i))
        test = bool(res)
        #assert b
        print(bool(res))
    tools.toolenrichments.append([str(tool), toolname, growin, growout, test])
    return g

def enrich_workflow( g, propagation ):
    n = n_triples(g)
    assert propagation
    import glob
    props = glob.glob('enrichments/propagate_'+propagation+'.ru')
    tests = glob.glob('enrichments/propagate_'+propagation+'_test.ru')
    for fn in (props):
        print('propagation '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        n_triples(g)
    for i in tests:
        print('Run propagation test '+i)
        res = g.query(file_to_str('rdf_prefixes.txt') + file_to_str(i))
        #assert b
        print(bool(res))
    return g

def test_workflow_lights( g ):
    """ Runs enrichments and tests for China night lights example workflow """
    print('> test_workflow_lights')
    _dir = "workflows/workflow_lights/"
    for fn in [_dir+"workflow_lights.ttl"]:
        print("Load N3 file: "+fn)
        g.parse( fn, format='n3' )
    g = run_rdfs_inferences( g )
    #g = enrich_workflow_tool( g, _dir )
    return g

def checkTool(operation):
    """
    Checks whether enrichment rules are available for operation class
    @param operation a GIS operation
    """
    #The list of tools to be used for tool enrichment
    lcptools = [ 'euclideandistance', 'polygontoraster','localmapalgebra','pointtoraster','costdistance','costpath','toline']
    operation = (((str(operation)).rpartition('#'))[2]).lower() #this extracts the toolname from its URI
    if operation in lcptools:
        return operation
    else:
        return 'NA'

#list of propagations
lcppropagations = ['qquality','path']

def reifyWorkflow(file, wfname):
    """ Adds reifications necessary to make a workflow wfname searchable """
    edge = rdflib.URIRef('http://geographicknowledge.de/vocab/Workflow.rdf#edge')
    subject = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#subject')
    predicate = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate')
    object = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#object')
    wf = rdflib.Graph()
    wfuri = rdflib.URIRef(wfname)
    wf.parse(file, format='n3')
    for s,p,o in wf:
        if(s!= wfuri):
            e = rdflib.BNode()
            wf.add((wfuri, edge, e))
            wf.add((e, subject, s))
            wf.add((e, predicate, p))
            wf.add((e, object, o))
    n_triples(wf)
    return wf

def test_workflow_lcpath( g ):
    """ Runs enrichments and tests for Least Cost Path example workflow """
    wfname = 'http://geographicknowledge.de/workflowLCP.rdf#lcpwf'
    print('> test_workflow_lights')
    _dir = "workflows/workflow_lcpath/"
    for fn in [_dir+"workflow_lcpath.ttl"]:
        print("Load N3 file: "+fn)
        g = reifyWorkflow(fn, wfname)+g
    g = run_rdfs_inferences( g )
    #prepare workflowgraph for DFS search. Order is important, because search requires rdfs inference
    wg = getWorkflowGraph(g,wfname)
    wg = load_ontologies(wg)
    wg = run_rdfs_inferences(wg)
    root = getRoot(wg)
    visited = set()
    # Run tool enrichments in the order of DFS backtracking through workflow graph
    print "Search through workflow and enrich!"
    DFSVisit(root, wg, visited, g)
    #Propagations are run in any order
    for i in lcppropagations:
        g = enrich_workflow( g, i )
    return g

def graph_to_file( g, output_filepath = None ):
    """ Serializes graph g to a n3 file """
    if not output_filepath:
        _outfn = 'output/workflows_output.ttl'
    else: _outfn = output_filepath
    g.serialize( _outfn, 'n3' )
    print("Written triples to " + _outfn)

#Methods for workflow DFS search
def getWorkflowGraph(g, wfname):
    print("extract workflow graph (for DFS):"+wfname)
    """Extracts a separate workflow graph of a given (named) workflow"""
    q = """ \n CONSTRUCT {?subject ?predicate ?object.}
       WHERE {
            ?wfname wf:edge ?edge.
            ?edge rdf:subject ?subject.
            ?edge rdf:predicate ?predicate.
            ?edge rdf:object ?object.
          FILTER (?wfname = <"""+wfname+""">)
       }"""
    q = file_to_str('rdf_prefixes.txt') + q
    #print q
    gwf = rdflib.Graph()
    qres = g.query(q)
    for i in qres:
        gwf.add(i)
    n_triples(gwf)
    return gwf


def getRoot(wg):
    """Gets the root in a (single) workflow graph"""
    start = ''
    output = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#output")
    for s,p,o in (wg.triples((None, output, None))):
        start = s
        break
    objects = getNeighbours(wg,start)
    while (len(objects)>0):
        start = objects[0]
        objects = getNeighbours(wg,start)
    print 'Root: '+ start
    return start

def DFSVisit(n, wg, visited, g):
    """Searches through workflow graph (wg) starting from n and enriches operation nodes in entire graph g in the order of backtracking"""
    # colors this node in grey
    visited.add(n)
    #print ('Just visited: '+str(n))
    for v in getNeighbours(wg, n, forward=False):
        if (v not in visited):
            DFSVisit(v, wg, visited, g)
    #print ('Just Colored Black: '+str(n))
    #Now backtracking starts
    operation = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#Operation")
    #get the operation types of the current node, check available enrichments for them, then enrich
    if (n, RDF.type, operation) in wg:
        print n
        for i in (wg.objects(subject=n, predicate=RDF.type)):
            op = checkTool(i)
            if (i != operation and op!='NA'):
                print op
                enrich_workflow_tool( g, op, n)


def getNeighbours(wg, n, forward=True):
    """Gets neighbors of nodes in a workflow graph, either forward (in the direction of the output(root)) or backward (in the direction of inputs)"""
    objects = []
    output = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#output")
    input = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#input")
    if forward:
        for i in (wg.objects(subject=n, predicate=output)):
                objects.append(i)
        for i in (wg.subjects(predicate=input,object=n)):
                objects.append(i)
    else:
        for i in (wg.subjects(predicate=output,object=n)):
                objects.append(i)
        for i in (wg.objects(subject=n,predicate=input)):
                objects.append(i)
    return objects

def main():
    # create inmemory store
    g = rdflib.ConjunctiveGraph()
    params = sys.argv[1:]

    g = load_ontologies( g )
    if 'lights' in params: g = test_workflow_lights( g )
    if 'lcpath' in params: g = test_workflow_lcpath( g )
    graph_to_file(g)
    
    print('Tool enrichments and tests:')
    print ("Final size: "+str(len(g)))
    #print "Test node:0"
    q = """ \n SELECT ?in2 ?ine ?inm ?out ?oute ?outm
       WHERE {
            {?node gis:inputdata ?in2.
            ?in2 ada:hasElement ?ine.
            ?ine ada:hasMeasure ?inm.
            FILTER (?node = <http://geographicknowledge.de/workflowLCP.rdf#0>)
            }
            UNION
            {?node wf:output ?out.
            ?out ada:hasElement ?oute.
            ?oute ada:hasMeasure ?outm.
            FILTER (?node = <http://geographicknowledge.de/workflowLCP.rdf#0>)
            }

       }"""
    q = file_to_str('rdf_prefixes.txt') + q
    #res = g.query(q)
    #for i in res:
        #pass
        #print i[0], i[1], i[2],i[3], i[4], i[5]
    order = ''
    print "Order of tool enrichments: "
    for j in tools.toolenrichments:
        order += ' :'+((((str(j[0])).rpartition('#'))[2]).lower())+' '
    print order
    print "Tool Toolname input output Test: "
    for i in sorted(tools.toolenrichments, key=lambda wf: wf[0]) :
        print i[0], i[1], i[2], i[3], i[4]
    
    print('OK') # end of script
    
if __name__ == '__main__':
    main()
