workflow is as follows. 

1.  clean up pdb with 
	source fix_pdb.sh
	fix_pdb -p proteinfile.pdb -s "selection text for vmd" -o out.pdb

2. construct alignment. use external tools such as uniprot and crystal for this.

3. bash run.sh will run the actual homology modelling. Keep in mind that myloop.py is the loop modelling class, this is where you need to write selection text for loop refinement 