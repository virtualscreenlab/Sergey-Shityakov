# to run the script go to File > Run > BSA_calculator.pml 
# if you are using this script, please cite: Shityakov, S.; Puskas, I.; Papai, K.; Salvador, E.; Roewer, N.; Forster, C.; Broscheit, J. A., 
# Sevoflurane-Sulfobutylether-beta-Cyclodextrin Complex: Preparation, Characterization, Cellular Toxicity, Molecular Modeling and 
# Blood-Brain Barrier Transport Studies. Molecules 2015, 20 (6), 10264-79.

h_add
flag ignore, none

set dot_solvent, 1
set dot_density, 3

host_area=cmd.get_area("bcd")
guest_area=cmd.get_area("pose")

create my_complex, bcd pose
complex_area=cmd.get_area("my_complex")
print((host_area+guest_area)-complex_area)/2

