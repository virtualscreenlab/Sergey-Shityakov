#!/usr/bin/python

import math # This will import math module 

psa = float(input("What is the polar surface area (PSA/TPSA) in A^2 for your compound?" ))
logp = float(input("What is the lipophilicity index (logP) for your compound?" ))
logbb = (0.152*(float(logp)) - 0.0148*(float(psa)) + 0.139) # this will calculate empirical Clark's logBB (blood/brain partition coefficient)
logbb_1 = (0.155*(float(logp)) - 0.01*(float(psa)) + 0.164) # this will calculate empirical Rishton's logBB (blood/brain partition coefficient)
print("logBB (Clark) =", logbb) # this will print out the results using Clark's equation
print("logBB (Rishton) =", logbb_1) # this will print out the results using Rishton's equation
print("(BBB-)0>logBB>0(BBB+)")

# before running the script go to https://www.molinspiration.com/cgi-bin/properties to calculate logP(miLogP) and PSA(TPSA)
# to run the script use this command: chmod +x logBB.py and then python logBB.py
# if you are using this script, please cite: Shityakov, S.; Salvador, E.; Pastorin, G.; Forster, C., Blood-brain barrier transport studies, aggregation, and molecular dynamics simulation of multiwalled carbon nanotube functionalized with fluorescein isothiocyanate. Int J Nanomedicine 2015, 10, 1703-13.
# Shityakov, S.; Forster, C., In silico predictive model to determine vector-mediated transport properties for the blood-brain barrier choline transporter. Adv Appl Bioinform Chem 2014, 7, 23-36.

