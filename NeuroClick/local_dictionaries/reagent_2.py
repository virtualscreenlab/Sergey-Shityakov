from rdkit import Chem

REAGENT_2 = {
    'Azide-alkyne cycloaddition': 'alkyne',
    'Diels-Alder': 'dienophile'
}

REAGENT_2_PATTERN = {
    'Azide-alkyne cycloaddition': Chem.MolFromSmarts('[#6]#[#6]'),
    'Diels-Alder': Chem.MolFromSmarts('[#6]#[#6]'),
    'Diels-Alder2': Chem.MolFromSmarts('[*]=[*]'),
}