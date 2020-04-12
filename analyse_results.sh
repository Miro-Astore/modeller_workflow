#!/bin/bash
#workflow/usage, specify modeller logfile (log.log by default in this workflow), this will output a .vmd file with the frames loaded in order of the lowest to highest DOPE scores (note that DOPE scores are negative because they are potentials. Most negative score is ostensibly the best model).


#cd ..
python modeller_workflow/find_order.py 
vmd -e  modeller_workflow/visualise_results_state.vmd $( cat ordered.txt )
#cd ../modeller_workflow
