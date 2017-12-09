#!/usr/bin/python

import math # This will import math module 

IC50 = float(input("What is your IC50 in microM?" ))
pIC50_value = -(math.log10(float(IC50)/float(1000000))) # this will calculate the pIC50 value from IC50 (microM)
print("pIC50 =", pIC50_value) # this will print out the results

IC50 = float(input("What is your IC50 in nM?" ))
pIC50_value1 = -(math.log10(float(IC50)/float(1000000000))) # this will calculate the pIC50 value from IC50 (nM)
print("pIC50 =", pIC50_value1) # this will print out the results

# to run the script use this command: python IC50_to_pIC50_converter.py
# if you are using this script, please cite: Shityakov, S.; Puskas, I.; Roewer, N.; Forster, C.; Broscheit, J., Three-dimensional quantitative structure-activity relationship and docking studies in a series of anthocyanin derivatives as cytochrome P450 3A4 inhibitors. Adv Appl Bioinform Chem 2014, 7, 11-21.

