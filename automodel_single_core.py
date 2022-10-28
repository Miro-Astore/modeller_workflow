from modeller import *
import multiprocessing
from modeller.automodel import *
from modeller.parallel import *
import numpy as np 

log.verbose()
env = environ()

env.io.atom_files_directory = ['./', './pdb_templates/','../']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms

temp_aln = Alignment(env)
temp_aln.read(file='../alignment_cleaned.ali')
#for i in temp_aln.keys()[1:]:
#    mdl = Model(env)
#    mdl.read(file=i, model_segment=('FIRST:@','FIRST:@'))
    #temp_aln.append_model(mdl)
template_files = temp_aln.keys()[1:]
#for i in range(len(template_files)):
#    template_files[i] = 'pdb_templates/' + template_files[i]

print(template_files)

#a = MyLoop(env,
#                alnfile  = 'alignment.ali',      # alignment filename
#                knowns   = ('pdbfile'),               # codes of the templates
#                sequence = 'rdrp',               # code of the target
#                loop_assess_methods=assess.DOPE) # assess each loop with DOPE

#a.loop.starting_model = 1           # First loop model
#a.loop.ending_model   = 10           # Last loop model
#a.loop.md_level = refine.very_slow # Loop model refinement level

env = Environ()
a = AutoModel(env,
                alnfile  = '../alignment_cleaned.ali',      # alignment filename
                knowns   = (template_files),               # codes of the templates
                sequence = 'akt2_complete',               # code of the target
                assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model = 1
a.ending_model = 500
a.make()
