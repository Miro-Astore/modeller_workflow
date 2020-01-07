from modeller import *
from modeller.automodel import *

class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('409:A', '435:A'), self.residue_range('834:B', '845:B'), self.residue_range('889:B', '900:B'), self.residue_range('1173:B', '1202:B'))
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B'],
                             renumber_residues=[1, 818])
        # Another way to label individual chains:
        self.chains[0].name = 'A'
        self.chains[1].name = 'B'
