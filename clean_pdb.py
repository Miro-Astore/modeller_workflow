import numpy as np
import sys
import re
import os 

#USAGE python modeller_workflow.py  PDB.pdb PDB_cleaned.pdb

out=open('/dev/shm/temp.pdb','w+')
FASTA=''
FASTA_DICT={'ARG':'R', 'SER':'S', 'ASN':'N', 'GLU':'E', 'GLN':'Q','TRP':'W','PRO':'P','HIS':'H','HSD':'H','LEU':'L','ILE':'I','LYS':'K','ALA':'A','CYS':'C','MET':'M','THR':'T','TYR':'Y','ASP':'N','VAL':'V','PHE':'F','GLY':'G'}

with open(sys.argv[-1]) as fp:
#with open('../6m71.pdb') as fp:
    line=fp.readline()
    cnt=1
    while line:
        obj = re.search('^ATOM',line)
        if obj:

            seq = re.search('AARG|ASER|AASN|AGLU|AGLN|ATRP|APRO|AHIS|AHSD|ALEU|AILE|ALYS|AALA|ACYS|AMET|ATHR|ATYR|AASP|AVAL|APHE|AGLY',line)
            if seq:
                seq = re.search('ARG|SER|ASN|GLU|GLN|TRP|PRO|HIS|HSD|LEU|ILE|LYS|ALA|CYS|MET|THR|TYR|ASP|VAL|PHE|GLY',line)
                thing = re.sub('A' + seq.group(0), ' ' + seq.group(0), line)
                out.write(thing)
                line=fp.readline()
            seq = re.search('[A-Z]ARG|[A-Z]SER|[A-Z]ASN|[A-Z]GLU|[A-Z]GLN|[A-Z]TRP|[A-Z]PRO|[A-Z]HIS|[A-Z]HSD|[A-Z]LEU|[A-Z]ILE|[A-Z]LYS|[A-Z]ALA|[A-Z]CYS|[A-Z]MET|[A-Z]THR|[A-Z]TYR|[A-Z]ASP|[A-Z]VAL|[A-Z]PHE|[A-Z]GLY',line)
            if seq:
                line=fp.readline()
                continue
            seq = re.search('ARG|SER|ASN|GLU|GLN|TRP|PRO|HIS|HSD|LEU|ILE|LYS|ALA|CYS|MET|THR|TYR|ASP|VAL|PHE|GLY',line)
            if seq:
                ca = re.search('CA',line)
                if ca:
                    res_type=seq.group(0)
                    FASTA = FASTA + str(FASTA_DICT[res_type])
                out.write(line)
                line=fp.readline()
                continue

        line=fp.readline()
        cnt=cnt+1

out.close()
os.rename()
