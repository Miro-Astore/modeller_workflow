import MDAnalysis as mda
import numpy as np
import sys
import os 
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import seq1
from Bio import SeqIO

file_list=np.loadtxt('pdb_list.txt',dtype=str)

os.chdir ('pdb_templates/')
records=[]

for i in file_list:
    u = mda.Universe(str(i) + '.pdb')
    all_res = u.select_atoms ('name CA and protein')
    chains = all_res.chainIDs
    chains =  set (chains)
    for j in chains :
        curr_chain_CAs = all_res.select_atoms('name CA and chainID ' + str(j) ) 
        curr_chain_all = u.select_atoms('protein and chainID ' + str(j) ) 
        curr_chain_all.write(str(i) + '_' + str(j) + '.pdb')
        resnames = seq1(''.join(curr_chain_CAs.resnames).capitalize())
        resnames= resnames + '*'
        #resnames = ' '.join(curr_chain_CAs.resnames).capitalize()
        fasta_name = str(i) + '_' + str(j) + '.fasta'

        record = SeqRecord(
               Seq(resnames),
               name = str(i) + '_' + str(j) + '.fasta',
               id=str(i) + '_' + str(j),
               description=str(i) + '_' + str(j)
        )
        records.append(record)

x = SeqIO.write(records, 'all_fasta.pir', "pir")


