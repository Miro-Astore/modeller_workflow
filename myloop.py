from modeller import *
from modeller.automodel import *

class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('114:', '143:'), self.residue_range('445:', '480:'))
