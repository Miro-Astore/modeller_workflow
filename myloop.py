from modeller import *
from modeller.automodel import *

class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('114:', '143:'), self.residue_range('445:', '480:'))
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B'],
                             renumber_residues=[1, 818])
        # Another way to label individual chains:
        self.chains[0].name = 'A'
        self.chains[1].name = 'B'
