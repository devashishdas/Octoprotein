#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
if len(sys.argv) < 4:
    print ("""
    [USAGE:] python BFactorCopy.py Protein_1(reference).pdb Protein_2(input).pdb Output.pdb 
          """)
    raise SystemExit

Reference_protein = sys.argv[1]
input_protein     = sys.argv[2]
output_protein    = sys.argv[3]

HOLD_BFACTOR = []

with open(output_protein,"w") as outfile:
    with open(Reference_protein) as ref:
        for lines in ref:
            if lines.startswith("ATOM") or lines.startswith("HETATM"):
                bfac = lines[61:66]
                HOLD_BFACTOR.append(bfac)
    with open(input_protein) as inp:
        x = 0
        for lines in inp:
            if lines.startswith("ATOM") or lines.startswith("HETATM"):
                outfile.write(lines[:61]+HOLD_BFACTOR[x]+lines[66:])
                x += 1
            else:
                outfile.write(lines)
