from modeller import *

log.verbose()
env = Environ()

env.io.atom_files_directory = ['./', './pdb_templates/','../']
env.libs.topology.read(file='$(LIB)/top_heav.lib')

# Read aligned structure(s):
aln = Alignment(env)
aln.append(file='alignment.ali', align_codes='all')
aln_block = len(aln)

# Read aligned sequence(s):
aln.append(file='akt2.ali', align_codes='akt2_complete')

# Structure sensitive variable gap penalty sequence-sequence alignment:
aln.salign(output='', max_gap_length=20,
                      gap_function=True,   # to use structure-dependent gap penalty
                      alignment_type='PAIRWISE', align_block=aln_block,
                      feature_weights=(1., 0., 0., 0., 0., 0.), overhang=0,
                      gap_penalties_1d=(-450, 0),
                      gap_penalties_2d=(0.35, 1.2, 0.9, 1.2, 0.6, 8.6, 1.2, 0., 0.),
                      similarity_flag=True)

aln.write(file='structure_ready_align.ali', alignment_format='PIR')
aln.write(file='structure_ready_align.pap', alignment_format='PAP')
