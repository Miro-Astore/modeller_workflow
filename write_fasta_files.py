import MDAnalysis as mda
import numpy as np
import sys
import os 
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import seq1

file_list=np.loadtxt('pdb_list.txt',dtype=str)

os.chdir ('templates_pdb/')

for i in file_list[0:1]:
    u = mda.Universe(str(i) + '.pdb')
    all_res = u.select_atoms ('name CA and protein')
    chains = all_res.chainIDs
    chains =  set (chains)
    for j in chains :
        curr_chain = all_res.select_atoms('chainID ' + str(j) ) 
        resnames = seq1(''.join(curr_chain.resnames).capitalize())
        resnames= resnames + '*'
        #resnames = ' '.join(curr_chain.resnames).capitalize()

        record = SeqRecord(
                Seq(resnames),
                name = str(i) + '_' + str(j) + '.fasta',

                id=str(i) + '_' + str(j)
        )
        #SeqIO.write(record, "fasta")
        print(record)

