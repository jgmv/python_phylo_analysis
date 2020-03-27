#!/usr/bin/python

'''
    File name: filter_fasta_seqs.py
    Author: Jose G. Macia-Vicente
    Date created: 2020-03-27
    Date last modified: 2020-03-27
    Python Version: 2.7
'''


from Bio import Phylo
import re
import sys
import argparse


parser = argparse.ArgumentParser(
    description='Convert phylogenetic trees to different formats: newick,\
    nexus, nexml, phyloxml, cdao.')

parser.add_argument(
    "i",
    help = 'input tree file')

parser.add_argument(
    "-o", help = 'output tree file',
    type=str,
    default='output.tre')

parser.add_argument(
    "-formatIn", help = 'input tree format',
    type=str,
    default='newick')

parser.add_argument(
    "-formatOut", help = 'tree format for output',
    type=str,
    default='nexus')

args = parser.parse_args()


if1 = args.i
if2 = args.formatIn
of1 = args.o
of2 = args.formatOut

Phylo.convert(if1, if2, of1, of2)

