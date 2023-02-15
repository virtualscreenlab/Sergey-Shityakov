from local_dictionaries.reactions import *
from local_dictionaries.reagent_1 import *
from local_dictionaries.reagent_2 import *

from time_functions import time_format

import time
from PyQt5 import QtGui
from rdkit import Chem


def neutralize_atoms(mol):
    pattern = Chem.MolFromSmarts("[N-]=[N+]")
    at_matches = mol.GetSubstructMatches(pattern)
    if len(at_matches) > 0:
        at_matches_list = [at_matches[0][0], at_matches[0][1]]
        for at_idx in at_matches_list:
            atom = mol.GetAtomWithIdx(at_idx)
            atom.SetFormalCharge(0)
            atom.UpdatePropertyCache()
    return mol


def iterate_reaction_sites(reaction_type, iterate_reactant, iterations, const_reactant, pattern, isomers, calc_window,
                           process_thread, type=1):
    prom_products = [iterate_reactant]
    for _ in range(iterations):
        next_products = []
        for mol in prom_products:
            if type == 1:
                out = pattern.RunReactants((mol, const_reactant))
            else:
                out = pattern.RunReactants((const_reactant, mol))
            if reaction_type == 'Azide-alkyne cycloaddition':
                next_products.extend([neutralize_atoms(mol[0]) for mol in out])
            else:
                next_products.extend([mol[0] for mol in out])

        try:
            prom_products = [Chem.CanonSmiles(Chem.MolToSmiles(product)) for product in
                             next_products]
        except Exception:
            prom_products = [Chem.MolToSmiles(product) for product in
                             next_products]
        prom_products = list(set(prom_products))
        prom_products = [Chem.MolFromSmiles(smi) for smi in prom_products]

    prom_products = [Chem.MolToSmiles(smi) for smi in prom_products]
    if prom_products == []:
        process_thread.print_signal.emit(
            f'Irrelevant reagents: {Chem.MolToSmiles(iterate_reactant)} and {Chem.MolToSmiles(const_reactant)} '
            f'for {reaction_type}. Something went wrong \n')
        calc_window.errors += 1
    return prom_products


def get_reaction_pattern(reaction_type, isomers, mol_2):
    if reaction_type == 'Azide-alkyne cycloaddition':
        if isomers == '1_4':
            pattern = REACTION[reaction_type][0]
        elif isomers == '1_5':
            pattern = REACTION[reaction_type][1]
        else:
            pattern = REACTION[reaction_type][2]
    else:
        if mol_2.HasSubstructMatch(REAGENT_2_PATTERN[reaction_type]):
            pattern = REACTION[reaction_type][0]
        else:
            pattern = REACTION[reaction_type][1]
    return pattern


def get_reaction_products(reagent_1, reagent_2, reaction_type, isomers, calc_window, process_thread):
    start_time = time.time()
    process_thread.print_signal.emit('Starting library generation...\n')

    if isomers is not None and isomers not in ['1_4', '1_5', 'both']:
        process_thread.print_signal.emit(f'Invalid isomers configuration: {isomers}')
        return

    calc_window.products = []
    calc_window.total_products = 0
    calc_window.all_candidates = 0
    calc_window.errors = 0

    for compound_1 in reagent_1:
        for compound_2 in reagent_2:
            calc_window.all_candidates += 1

            reactants = (Chem.MolFromSmiles(compound_1), Chem.MolFromSmiles(compound_2))
            compound_1_count = len(reactants[0].GetSubstructMatches(REAGENT_1_PATTERN[reaction_type]))
            compound_2_count = len(reactants[1].GetSubstructMatches(REAGENT_2_PATTERN[reaction_type]))
            if compound_2_count == 0 and reaction_type == 'Diels-Alder':
                compound_2_count = len(reactants[1].GetSubstructMatches(REAGENT_2_PATTERN[reaction_type + '2']))

            pattern = get_reaction_pattern(reaction_type, isomers, reactants[1])

            try:
                if (compound_1_count > 1) and (compound_2_count > 1):
                    process_thread.print_signal.emit(
                        f'Warning: troubles generating molecule from {compound_1} and {compound_2}. '
                        f'Both species contain multiple reaction sites. '
                        f'You should remain only 1 reaction site in at least one reagent\n')
                    calc_window.errors += 1
                    continue

                elif compound_1_count > 1:
                    prom_products = iterate_reaction_sites(reaction_type, reactants[0], compound_1_count, reactants[1],
                                                           pattern, isomers, calc_window, process_thread, type=1)

                else:
                    prom_products = iterate_reaction_sites(reaction_type, reactants[1], compound_2_count, reactants[0],
                                                           pattern, isomers, calc_window, process_thread, type=2)
            except Exception:
                process_thread.print_signal.emit(f'Irrelevant reagents: {compound_1} and {compound_2}\n')
                calc_window.errors += 1
                continue

            calc_window.total_products += len(prom_products)

            calc_window.products.extend(prom_products)

            process_thread.msleep(calc_window.timeout)

        calc_window.log.moveCursor(QtGui.QTextCursor.End)

    end_time = time.time()
    calc_window.hours, calc_window.minutes, calc_window.seconds = time_format(start_time, end_time)

    calc_window.activate_next(process=True)
    return calc_window.products


def form_stats_log(calc_window, hours, minutes, seconds, reagent_1, reagent_2, total_products, errors):
    calc_window.show_log('\n\n')
    calc_window.show_log('====\n')
    calc_window.show_log('Finished library generation!\n')
    calc_window.show_log(f'Time: {hours:02}:{minutes:02}:{seconds:02}.\n')

    calc_window.show_log(
        f'{total_products} compounds were generated from {len(reagent_2)} {REAGENT_2[calc_window.reaction_type]} and '
        f'{len(reagent_1)} {REAGENT_1[calc_window.reaction_type]}.\n')

    calc_window.show_log(f'Failed to construct {errors} molecules.\n')


def reaction(isomers, calc_window, process_thread):
    if not calc_window.reagent_1:
        process_thread.print_signal.emit(
            f'Invalid {REAGENT_1[calc_window.reaction_type]} configuration was entered. Unable to continue')
        return

    if not calc_window.reagent_2:
        process_thread.print_signal.emit(
            f'Invalid {REAGENT_2[calc_window.reaction_type]} configuration was entered. Unable to continue')
        return

    reaction_products = get_reaction_products(calc_window.reagent_1, calc_window.reagent_2, calc_window.reaction_type,
                                              isomers, calc_window, process_thread)
    with open('products.txt', 'w') as f:
        for mol in reaction_products:
            f.write(f'{mol}\n')
