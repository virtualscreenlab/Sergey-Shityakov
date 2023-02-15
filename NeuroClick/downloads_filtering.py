import os
import pandas as pd

INFO_COLS = ['Canonical SMILES', 'Molecule', 'ESOL Solubility (mg/ml)', 'Ali Solubility (mg/ml)',
             'Silicos-IT Solubility (mg/ml)', 'ESOL Solubility (mol/l)', 'Ali Solubility (mol/l)',
             'Silicos-IT Solubility (mol/l)', 'ESOL Class', 'Ali Class', 'Silicos-IT class']


def delete_former_results(files):
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


def filter(step, df, cols_to_use, threshold_cols, violations_cols, gi_level, saving_format):
    if step == 0:
        delete_former_results(['output.txt', 'output.csv'])
    for col in cols_to_use:
        if col in threshold_cols:
            df = df[
                (df[col].astype(float) >= threshold_cols[col][0]) & (df[col].astype(float) <= threshold_cols[col][1])]
        elif col in violations_cols:
            df = df[df[col] <= violations_cols[col]]
        elif col == 'GI absorption':
            df = df[df[col] == gi_level]
        else:
            if col not in INFO_COLS:
                df = df[df[col] == 'Yes']
    with open('output.txt', 'a'):
       df['Canonical SMILES'].to_csv(r'output.txt', header=None, index=None, sep=' ', mode='a')
    if saving_format == 'csv':
        try:
            old_df = pd.read_csv('output.csv')
            merged_df = pd.concat([old_df, df], ignore_index=True)
            del merged_df['Molecule']
            merged_df.to_csv('output.csv', index=False)
        except:
            del df['Molecule']
            df.to_csv('output.csv', index=False)
