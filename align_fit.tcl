mol new best.pdb 
mol new 6m71.pdb 
set sel [atomselect 0 "name CA and resid 200 to 800 "]
set res [$sel get resid ]


set sel1 [atomselect 1 "name CA and resid $res and  chain A "]
set res [$sel1 get resid ]

set sel [atomselect 0 "name CA and resid $res "]
set M [measure fit $sel $sel1]
set sel [atomselect 0 "all"]

$sel move $M 

