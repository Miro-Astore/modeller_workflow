from modeller import *

log.verbose()
env = Environ()


env.io.atom_files_directory = ['./', './pdb_templates/','../']

#-- Prepare the input files

#-- Read in the sequence database
sdb = SequenceDB(env)
sdb.read(seq_database_file='pdb_templates/all_fasta.fasta', seq_database_format='FASTA',
                  chains_list='pdb_templates/chains_list.txt', minmax_db_seq_len=(1, 4000), clean_sequences=True)
                  #chains_list='ALL', minmax_db_seq_len=(1, 4000), clean_sequences=True)

for i in range(len(sdb)):
    sdb[i].atom_file = sdb[i].code

#-- Write the sequence database in binary form
sdb.write(seq_database_file='all_fasta.bin', seq_database_format='BINARY',
                    chains_list='pdb_templates/chains_list.txt')
                    #chains_list='ALL')

#-- Now, read in the binary database
sdb.read(seq_database_file='all_fasta.bin', seq_database_format='BINARY',
                  chains_list='pdb_templates/chains_list.txt')
                  #chains_list='ALL')

#-- Read in the target sequence/alignment
aln = Alignment(env)
aln.append(file='akt2.ali', alignment_format='PIR', align_codes='ALL')

#-- Convert the input sequence/alignment into
#   profile format
prf = aln.to_profile()

#-- Scan sequence database to pick up homologous sequences
print("BUILDING ALIGNMENT PROFILE")

prf.build(sdb, matrix_offset=-450.0, rr_file='${LIB}/blosum62.sim.mat',
                    gap_penalties_1d=(-500, -50), n_prof_iterations=1,
                    check_profile=False, max_aln_evalue=0.60)

#-- Write out the profile in text format
prf.write(file='build_profile.prf', profile_format='TEXT')

#-- Convert the profile back to alignment format
aln = prf.to_alignment()

for i in aln.keys()[1:-1]:
    aln[i].prottyp = 'structure'

for i in aln.keys()[1:-1]:
    mdl = Model (env)
    mdl.read(i)
    first_res = mdl.residues[0].num
    last_res = mdl.residues[-1].num


#-- Write out the alignment file
aln.write(file='alignment.ali', alignment_format='PIR')
