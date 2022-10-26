from modeller import *
import multiprocessing
from modeller.automodel import *
from modeller.parallel import *
from myloop import MyLoop
from mymodel import MyModel
import numpy as np 

log.verbose()
env = environ()

env.io.atom_files_directory = ['./', './pdb_templates/','../']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms

temp_aln = Alignment(env)
temp_aln.read(file='alignment.ali')
template_files = temp_aln.keys()[1:]
#for i in range(len(template_files)):
#    template_files[i] = template_files[i] + '.pdb'

print(template_files)
a = MyModel(env,
                alnfile  = 'alignment.ali',      # alignment filename
                knowns   = template_files,               # codes of the templates
                sequence = 'akt2_complete',               # code of the target
                assess_methods=assess.DOPE) # assess each loop with DOPE

#a = MyLoop(env,
#                alnfile  = 'alignment.ali',      # alignment filename
#                knowns   = ('pdbfile'),               # codes of the templates
#                sequence = 'rdrp',               # code of the target
#                loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1 # index of the first model
a.ending_model  = 50 # index of the last model

#a.loop.starting_model = 1           # First loop model
#a.loop.ending_model   = 10           # Last loop model
#a.loop.md_level = refine.very_slow # Loop model refinement level

j = job()
cpu_num= multiprocessing.cpu_count()
for i in range(cpu_num):
    j.append(local_slave())

a.use_parallel_job(j) # do modeling and loop refinement
a.make()
