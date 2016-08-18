#
# SemGeoWorkflows project
# Makefile
#

all: clean
	python semworkflows.py lcpath lights

l: clean
	python semworkflows.py lights

p: clean
	python semworkflows.py lcpath
	
q:
	python semworkflows.py questions
	
clean:
	-@rm output/*

err:
	-@grep -i error output/workflows_output.rdf