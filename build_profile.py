from modeller import *
import numpy as np 

log.verbose()
env = Environ()


env.io.atom_files_directory = ['./', './pdb_templates/','../']

#-- Prepare the input files

#-- Read in the sequence database
#for (code, chain) in (('2mdh', 'A'), ('1bdm', 'A'), ('1b8p', 'A')):
#    mdl = Model(env, file=code, model_segment=('FIRST:'+chain, 'LAST:'+chain))
#    aln.append_model(mdl, atom_files=code, align_codes=code+chain)
chains_list = np.loadtxt('pdb_templates/chains_list.txt',dtype=str)
aln = Alignment(env)
for i in chains_list:
    pdb_code = i
    chainID = i.split('_')[-1]
    mdl = Model(env, file=pdb_code, model_segment=('FIRST:'+chainID, 'LAST:'+chainID), keep_disulfides=True)
    aln.append_model(mdl, atom_files=pdb_code, align_codes=pdb_code)

aln.write('pdb_templates/template_sequences.pir',alignment_format='PIR',alignment_features='',align_alignment=False)

#exit()
sdb = SequenceDB(env)
sdb.read(seq_database_file='pdb_templates/template_sequences.pir', seq_database_format='PIR',
                  chains_list='pdb_templates/chains_list.txt', minmax_db_seq_len=(1, 4000), clean_sequences=True)
                  #chains_list='ALL', minmax_db_seq_len=(1, 4000), clean_sequences=True)

for i in range(len(sdb)):
    #print(dir(sdb[i]))
    print(sdb[i].residues)

#-- Write the sequence database in binary form
sdb.write(seq_database_file='seqs.bin', seq_database_format='BINARY',
                    chains_list='pdb_templates/chains_list.txt')
                    #chains_list='ALL')

sdb.write(seq_database_file='seqs.pir', seq_database_format='pir',
                    chains_list='pdb_templates/chains_list.txt')

#-- Now, read in the binary database
sdb.read(seq_database_file='seqs.bin', seq_database_format='BINARY',
                  chains_list='pdb_templates/chains_list.txt')
                  #chains_list='ALL')

#-- Read in the target sequence/alignment
aln = Alignment(env)
aln.append(file='akt2.ali', alignment_format='PIR', align_codes='ALL')

#-- Convert the input sequence/alignment into
#   profile format

#-- Scan sequence database to pick up homologous sequences
print("BUILDING ALIGNMENT PROFILE")

#-- Write out the profile in text format
prf = aln.to_profile()

prf.build(sdb, matrix_offset=-450.0, rr_file='${LIB}/blosum62.sim.mat',
                    gap_penalties_1d=(-500, -50), n_prof_iterations=1,
                    check_profile=False, max_aln_evalue=0.60, gaps_in_target=True)

prf.write(file='build_profile.prf', profile_format='TEXT')

#-- Convert the profile back to alignment format
aln = prf.to_alignment()


#for i in aln.keys()[1:]:
#    mdl = Model (env)
#    aln[i].reread()
#    mdl.read(i,model_segment=('FIRST:@','LAST:@'))
#    first_res = mdl.residues[0].num
#    last_res = mdl.residues[-1].num
#    chain_name = aln[i].chains[0].name
#    mdl.rename_segments(segment_ids=chain_name)

    #aln[i].residue_range = mdl.residue_range()
##    print(aln[i])
#    aln[i].chains[0].name = 'A'
#    print(dir(aln[i]))
#    #print(aln[i].chains[0].name)
##    ##print(dir(aln[i]))
##    #print(dir(aln[i].residue_range))

#for i in aln.keys()[1:]:
#    aln[i].prottyp = 'structure'
#    mdl = Model (env)
#    mdl.read(i)
#    first_res = mdl.residues[0].num
#    last_res = mdl.residues[-1].num
##    #aln[i].residue_range = mdl.residue_range()
##    print(aln[i])
#    aln[i].chains[0].name = 'A'
#    print(dir(aln[i]))
#    #print(aln[i].chains[0].name)
##    ##print(dir(aln[i]))
##    #print(dir(aln[i].residue_range))


#print(dir(aln[i]))
#aln[i].segments[0].chain_name = 'A'
#aln[i].segments[0].name = 'A'
#print(aln[i].segments[0].name)
#-- Write out the alignment file
aln.write(file='alignment.ali', alignment_format='PIR')

