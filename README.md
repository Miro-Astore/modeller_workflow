#TODO, more MDAnalysis conversion work. Work out how to use modeller to do the alignment for you.
workflow is as follows. 

1.  clean up pdb with 
	source fix_pdb.sh
	fix_pdb -p proteinfile.pdb -s "selection text for vmd" -o out.pdb

2. construct alignment. use external tools such as uniprot and crystal for this. https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins

3. bash run.sh will run the actual homology modelling. Keep in mind that myloop.py is the loop modelling class, this is where you need to write selection text for loop refinement. Will output everything to modeller.log 

4. To view results run bash modeller_workflow/analyze_results.sh and make sure you are in linux with vmd installed.


