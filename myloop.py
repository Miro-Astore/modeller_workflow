from modeller import *
from modeller.automodel import *

class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('1:', '30:'),self.residue_range('52:','69:'),self.residue_range('103:','111:'),self.residue_range('896:','905:'),self.residue_range('920:','932:'))
#    def special_patches(self, aln):
#        # Rename both chains and renumber the residues in each
#        self.rename_segments(segment_ids=['A', 'B'],
#                             renumber_residues=[1, 818])
#        # Another way to label individual chains:
#        self.chains[0].name = 'A'
#        self.chains[1].name = 'B'
