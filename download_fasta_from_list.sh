cwd=$(pwd)

cd fasta_seqs
rm all_fasta.txt 
for pdb_id in $(cat ../pdb_list.txt);
do
	curl "https://www.rcsb.org/fasta/entry/$pdb_id" > $(echo $pdb_id | sed "s/\.pdb//g").fasta
	if [ -f all_fasta.txt ]
	then 
		cat $(echo $pdb_id | sed "s/\.pdb//g").fasta >> all_fasta.txt 
	else 
		cat $(echo $pdb_id | sed "s/\.pdb//g").fasta > all_fasta.txt
	fi 
done

cat *fasta > all_fasta.txt
cd $cwd
