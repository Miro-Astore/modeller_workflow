#!/bin/bash
## usage
# source fix_pdb.sh
# fix_pdb -p <pdb_file> -s "atomselection text" -o <output_pdb_file>
fix_pdb () { 
    OPTIND=1
    while getopts "p:s:o:" OPTION; do

	case $OPTION in 
	    p) 
	       echo $OPTARG
	       python clean_pdb.py $OPTARG
	       ;;
	    s) 
		   echo $OPTARG
		   #echo "mol new /dev/shm/temp.pdb" > /dev/shm/temp.tcl
		   #echo "set sel [atomselect top \"$OPTARG\"] " >> /dev/shm/temp.tcl
		   #echo "\$sel writepdb /dev/shm/temp2.pdb" >> /dev/shm/temp.tcl
		   #echo "exit" >> /dev/shm/temp.tcl

		   #vmd -dispdev text  -e /dev/shm/temp.tcl
		   python write_sel.py /dev/shm/temp.pdb "$OPTARG" /dev/shm/temp2.pdb 
		   ;;
	    o) 
			echo $OPTARG
			mv /dev/shm/temp2.pdb $(echo $OPTARG | sed "s/\.pdb//g").pdb
			mv /dev/shm/temp2.fasta $(echo $OPTARG | sed "s/\.pdb//g").fasta
			if [ ! $? -eq 0 ]
			then
				rm /dev/shm/temp2.pdb
				rm /dev/shm/temp2.fasta
			fi
			;;
	esac
    done 
}
