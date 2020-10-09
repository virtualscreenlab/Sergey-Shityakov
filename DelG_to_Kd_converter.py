#!/usr/bin/python

import math # This will import math module

delg = float(input("What is your DelG in kcal/mol?" ))
R = 1.9872 #cal/K.mol
T = 298.18 #in degrees Kelvin - Body temperature
Kd_value = math.exp((-delg*1000)/(R*T)) # this will calculate the dissociation constant from the Gibbs free energy of binding
Kd_value1 = (math.exp((-delg*1000)/(R*T)))*1000000 # this will calculate the dissociation constant from the Gibbs free energy of binding
Kd_value2 = (math.exp((-delg*1000)/(R*T)))*1000000000 # this will calculate the dissociation constant from the Gibbs free energy of binding
print("Kd =", "{:e}".format(Kd_value), "M") # this will print out the results in M
print("Kd =", "{:e}".format(Kd_value1), "microM") # this will print out the results in microM
print("Kd =", "{:e}".format(Kd_value2), "nM") # this will print out the results in nM

# to run the script in terminal use this command: python DelG_to_Kd_converter.py
# if you are using this script, please cite: Shityakov, S.; Broscheit, J.; Forster, C., alpha-Cyclodextrin dimer complexes of dopamine and levodopa derivatives to assess drug delivery to the central nervous system: ADME and molecular docking studies. Int J Nanomedicine 2012, 7, 3211-9.
# edited by Sebastian Moes
