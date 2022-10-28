from modeller import *
import numpy as np 

env = Environ()
aln = Alignment(env)

env.io.atom_files_directory = ['./', './pdb_templates/','../']

chains_list = np.loadtxt('pdb_templates/chains_list.txt',dtype=str)
aln_read_pdbs = Alignment(env)
for i in chains_list:
    pdb_code = i
    chainID = i.split('_')[-1]
    mdl = Model(env, file=pdb_code, model_segment=('FIRST:'+chainID, 'LAST:'+chainID), keep_disulfides=True)
    aln.append_model(mdl, atom_files=pdb_code, align_codes=pdb_code)

aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)

