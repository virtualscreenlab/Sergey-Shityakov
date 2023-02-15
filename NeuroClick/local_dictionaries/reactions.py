from rdkit.Chem import rdChemReactions

REACTION = {
    'Azide-alkyne cycloaddition': [rdChemReactions.ReactionFromSmarts(
        '[*:6][N:1]=[N:2]=[N:3].[#6:7][C:4]#[C:5]>>[*:6][N:1]([N:2]=[N:3]1)[C:5]=[C:4]1[#6:7]'),
        rdChemReactions.ReactionFromSmarts(
            '[*:6][N:1]=[N:2]=[N:3].[#6:7][C:4]#[C:5]>>[*:6][N:1]1[N:2]=[N:3][C:4]=[C:5]1[#6:7]'),
        rdChemReactions.ReactionFromSmarts('[*:6][N:1]=[N:2]=[N:3].[C:4]#[C:5]>>[*:6][N:1]1[N:2]=[N:3][C:4]=[C:5]1')
    ],
    'Diels-Alder': [rdChemReactions.ReactionFromSmarts(
        '[#6:1]=[#6:2][#6:3]=[#6:4].[#6:5]#[#6:6]>>[#6:1]1[#6:2]=[#6:3][#6:4][#6:5]=[#6:6]1'),
        rdChemReactions.ReactionFromSmarts(
        '[#6:1]=[#6:2][#6:3]=[#6:4].[*:5]=[*:6]>>[#6:1]1[#6:2]=[#6:3][#6:4][#6:5][#6:6]1')
    ]
}
