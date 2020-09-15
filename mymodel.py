from modeller import *
from modeller.automodel import *

class MyModel(automodel):
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B'],
                             renumber_residues=[1, 791])
        # Another way to label individual chains:
        self.chains[0].name = 'A'
        self.chains[1].name = 'B'
    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
        #       Add some restraints from a file:
        #       rsr.append(file='my_rsrs1.rsr')

        #       Residues 20 through 30 should be an alpha helix:
        rsr.add(secondary_structure.alpha(self.residue_range('801:B', '811:B')))
        #       beta-strands:
        #rsr.add(secondary_structure.strand(self.residue_range('818:B', '825:B')))
        #       An anti-parallel sheet composed of the two strands:
        #rsr.add(secondary_structure.sheet(at['N:1'], at['O:14'], sheet_h_bonds=-5))
        #       Use the following instead for a *parallel* sheet:
        #       rsr.add(secondary_structure.sheet(at['N:1'], at['O:9'],
        #                                         sheet_h_bonds=5))

        #       Restrain the specified CA-CA distance to 10 angstroms (st. dev.=0.1)
        #       Use a harmonic potential and X-Y distance group.
        #rsr.add(forms.gaussian(group=physical.xy_distance,
        #                    feature=features.distance(at['CA:35'],
        #                    at['CA:40']),
        #                    mean=10.0, stdev=0.1))
