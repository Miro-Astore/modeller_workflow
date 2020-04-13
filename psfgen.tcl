package require psfgen

topology /home/miro/Downloads/toppar/top_all36_prot.rtf
#topology /home/miro/Downloads/toppar/par_all36_cgenff.prm
topology /home/miro/Downloads/toppar/toppar_water_ions.str


pdbalias residue HIS HSD 
pdbalias residue ZN ZN2 
pdbalias atom ILE  CD1 CD
segment AP1 {
	first NONE
	last NONE
	pdb moved_A.pdb
}
coordpdb moved_A.pdb AP1

segment BP1 {
	first NONE
	last NONE
	pdb B.pdb
}
coordpdb B.pdb BP1

segment CP1 {
	first NONE
	last NONE
	pdb C.pdb
}
coordpdb C.pdb CP1

segment DP1 {
	first NONE
	last NONE
	pdb D.pdb
}
coordpdb D.pdb DP1

guesscoord
writepdb prot.pdb
writepsf prot.psf

exit
