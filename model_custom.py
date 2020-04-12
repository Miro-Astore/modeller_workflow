from modeller import *
import multiprocessing
from modeller.automodel import *
from modeller.parallel import *
from myloop import MyLoop

log.verbose()
env = environ()

env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms

a = MyLoop(env,
                alnfile  = 'alignment.ali',      # alignment filename
                knowns   = ('6m71_prot'),               # codes of the templates
                sequence = 'rdrp',               # code of the target
                loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1 # index of the first model
a.ending_model  = 5 # index of the last model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 10           # Last loop model
a.loop.md_level = refine.very_slow # Loop model refinement level

j = job()
cpu_num= multiprocessing.cpu_count()
for i in range(cpu_num):
    j.append(local_slave())

a.use_parallel_job(j) # do modeling and loop refinement
a.make()
