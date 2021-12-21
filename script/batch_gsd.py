#!/usr/bin/env python
#import sys
#sys.path.append("/home/gthemudo/bin/genomic_sequence_downloader.py/script/")
import subprocess
#import genomic_sequence_downloader_themudo as gsd

filename = 'gsd.input'
species_list = '../species_list.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for line in lines:
    #parse line to get all the parameters:
    genes = line.split()
    target_gene = genes[0]
    d1 = genes[1]
    d2 = genes[2]
    d3 = genes[3]
    u1 = genes[4]
    u2 = genes[5]
    u3 = genes[6]
    target_seq = target_gene + '_seq.fas'
    target_out = target_gene + '.out'
    cmd = ['python', '/home/gthemudo/bin/genomic_sequence_downloader.py/script/genomic_sequence_downloader_themudo.py', target_gene , d1, d2, d3, u1, u2, u3, species_list, target_seq, target_out]
    subprocess.run(cmd)
