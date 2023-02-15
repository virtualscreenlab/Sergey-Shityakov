from rdkit import Chem

REAGENT_1 = {
    'Azide-alkyne cycloaddition': 'azide',
    'Diels-Alder': 'diene'
}

REAGENT_1_PATTERN = {
    'Azide-alkyne cycloaddition': Chem.MolFromSmarts('[N]=[N]=[N]'),
    'Diels-Alder': Chem.MolFromSmarts('[#6]=[#6][#6]=[#6]')

}