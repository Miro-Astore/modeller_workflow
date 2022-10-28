from modeller import *

log.verbose()
env = Environ()

env.io.atom_files_directory = ['./', './pdb_templates/','../']

#aln = Alignment(env, file='alignment.ali')
 
#aln.salign(overhang=30, gap_penalties_1d=(-450, -50),
#                      alignment_type='tree', output='ALIGNMENT')
 
#aln.write(file='malign.ali', alignment_format='PIR')



aln = Alignment(env, file='alignment.ali', align_codes='all')
aln.salign(rr_file='$(LIB)/as1.sim.mat',  # Substitution matrix used
                      output='',
                      max_gap_length=20,
                      gap_function=True,              # If False then align2d not done
                      feature_weights=(1., 0., 0., 0., 0., 0.),
                      gap_penalties_1d=(-100, 0),
                      gap_penalties_2d=(3.5, 3.5, 3.5, 0.2, 4.0, 6.5, 2.0, 0.0, 0.0),
                      # d.p. score matrix
                      #output_weights_file='salign.mtx'
                      similarity_flag=True)   # Ensuring that the dynamic programming
                                   # matrix is not scaled to a difference matrix
aln.write(file='align2d.ali', alignment_format='PIR')
aln.write(file='align2d.pap', alignment_format='PAP')

