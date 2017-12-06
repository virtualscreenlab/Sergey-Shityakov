#!/usr/bin/python

import math # This will import math module 

delg = float(input("What is your DelG in kcal/mol?" ))
Kd_value = math.exp((delg*1000)/(1.98*298.15)) # his will calculate the dissociation constant from the Gibbs free energy of binding
Kd_value1 = (math.exp((delg*1000)/(1.98*298.15)))*1000000 # This will calculate the dissociation constant from the Gibbs free energy of binding
Kd_value2 = (math.exp((delg*1000)/(1.98*298.15)))*1000000000 # his will calculate the dissociation constant from the Gibbs free energy of binding
print("Kd =", Kd_value, "M") # This will print out the results in M
print("Kd =", Kd_value1, "microM") # This will print out the results in microM
print("Kd =", Kd_value2, "nM") # This will print out the results in nM

# if you are using this script please cite: Shityakov, S.; Broscheit, J.; Forster, C., alpha-Cyclodextrin dimer complexes of dopamine and levodopa derivatives to assess drug delivery to the central nervous system: ADME and molecular docking studies. Int J Nanomedicine 2012, 7, 3211-9.
