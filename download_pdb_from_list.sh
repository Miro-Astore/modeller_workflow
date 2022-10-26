cat blastp_output.txt | grep \>  | awk -F_ '{print $1}'  | sed "s/>//g" > pdb_list.txt
cwd=$(pwd)
cd pdb_templates
cat ../blastp_output.txt | grep \>  | awk '{print $1}' >  chains_list.txt
for pdb_id in $(cat ../pdb_list.txt);
do
	if [ ! -f $pdb_id.pdb ] 
	then
		wget https://files.rcsb.org/download/$pdb_id.pdb
	fi
done

cd $cwd
