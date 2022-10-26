
for i in $(cat pdb_list.txt); 
do
python modeller_workflow/clean_pdb.py $i

done
