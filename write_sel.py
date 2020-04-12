import MDAnalysis as mda
import re
import numpy as np
import sys 

PDB=sys.argv[1]
SEL=sys.argv[2]
OUT=sys.argv[3]
u=mda.Universe(PDB)
sel=u.select_atoms(SEL)
sel.write(OUT)

FASTA=''
FASTA_DICT={'ARG':'R', 'SER':'S', 'ASN':'N', 'GLU':'E', 'GLN':'Q','TRP':'W','PRO':'P','HIS':'H','HSD':'H','LEU':'L','ILE':'I','LYS':'K','ALA':'A','CYS':'C','MET':'M','THR':'T','TYR':'Y','ASP':'D','VAL':'V','PHE':'F','GLY':'G'}
print(OUT)

FASTA_OUT=open(str(OUT)[:-4] + '.fasta','w+')
with open(OUT) as fp:
#with open('../6m71.pdb') as fp:
    Lines=fp.readlines()
    for line in Lines:
        cnt=1
        print(line)
        obj = re.search('^ATOM',line)
        if obj:
            seq = re.search('ARG|SER|ASN|GLU|GLN|TRP|PRO|HIS|HSD|LEU|ILE|LYS|ALA|CYS|MET|THR|TYR|ASP|VAL|PHE|GLY',line)
            if seq:
                ca = re.search('CA',line)
                if ca:
                    res_type=seq.group(0)
                    FASTA = FASTA + str(FASTA_DICT[res_type])


#with  open(OUT) as fp:
#    line=fp.readline()
#    print(line)
#    seq = re.search('ARG|SER|ASN|GLU|GLN|TRP|PRO|HIS|HSD|LEU|ILE|LYS|ALA|CYS|MET|THR|TYR|ASP|VAL|PHE|GLY',line)
#    if seq:
#        ca = re.search('CA',line)
#        if ca:
#            res_type=seq.group(0)
#            FASTA = FASTA + str(FASTA_DICT[res_type])
#    line=fp.readline()
#print(FASTA)
FASTA_OUT.write(FASTA)
FASTA_OUT.close()
