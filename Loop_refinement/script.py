from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP

def process_pdb(pdb_file):
    # Load the PDB file
    pdb_parser = PDBParser(QUIET=True)
    structure = pdb_parser.get_structure(pdb_file, pdb_file)

    # Initialize DSSP
    dssp = DSSP(structure[0], pdb_file)

    # Extract secondary structure information
    secondary_structure = {}
    for residue in dssp:
        chain_id = residue[0][0]
        res_id = residue[0][1]
        ss = residue[2]
        if chain_id not in secondary_structure:
            secondary_structure[chain_id] = {}
        secondary_structure[chain_id][res_id] = ss

    # Print the secondary structure
    for chain_id, residues in secondary_structure.items():
        for res_id, ss in sorted(residues.items()):
            print(f"Chain {chain_id}, Residue {res_id}: {ss}")

    # Save the sequence without loops
    seq_no_loops = ""
    for chain_id, residues in secondary_structure.items():
        for res_id, ss in sorted(residues.items()):
            if ss != ' ' and (not (410 <= res_id <= 503) and not (765 <= res_id <= 830)):
                seq_no_loops += ss

    return seq_no_loops

# Usage
pdb_file = "alfafold3-pul56.pdb"
sequence_without_loops = process_pdb(pdb_file)
print("Sequence without loops:", sequence_without_loops)
