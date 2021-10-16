# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSv61ejXESrp34CUz1PqZCsoA43tzc8y

**Task 06: Modifying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
for s, p, o in g:
  print(s,p,o)

g.add((ns.JaneSmith, VCARD.FN, Literal("Jane Smith")))
g.add((ns.JaneSmith, VCARD.Given, Literal("Jane")))
g.add((ns.JaneSmith, VCARD.Family, Literal("Smith")))
for s, p, o in g.triplets((ns.JaneSmith, None, None)):
  print(s,p,o)

g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JaneSmith, VCARD.work, ns.UPM))
for s, p, o in g.triplets((ns.JaneSmith, None, None)):
  print(s,p,o)