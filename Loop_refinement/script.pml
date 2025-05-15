# Load the PDB file
load alfafold3-pul56.pdb
#save seq_total.fasta

# Set the display style to cartoon
show_as cartoon

# Color beta sheets (S) forest green
color forest, ss S

# Color alpha helices (H) firebrick red
color firebrick, ss H

# Color non-sheet and non-helix elements (loops, etc.) white. 
color white, ss L

# Longer loops, such as ω-loops or composite turns, can range from 9 to 15 residues or more. 
select loop_1, chain A and resi 410-503
select loop_2, chain A and resi 765-830
#remove loop_1
#remove loop_2

#save seq_no_loops.fasta

# Optional: Adjust the view and rendering (uncomment if desired)
zoom
set cartoon_fancy_helices, 1
#set cartoon_highlight_color, white

save model_no_loops.pdb