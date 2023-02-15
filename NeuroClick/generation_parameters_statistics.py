import calculations
from base_window import BaseWindow

from PyQt5 import QtWidgets


class ParametersStatisticsWindow(BaseWindow):
    def __init__(self, start_window, saving_options_window, selected_isomers, inner_alkynes_specification,
                 Lipinski_descriptors, Ghose_descriptors, Veber_descriptors, Egan_descriptors, QED_descriptors,
                 Muegge_descriptors, Leadlikeness_descriptors, logBB_model, threshold, saving_format):
        super().__init__()

        self.log = QtWidgets.QTextEdit(self)
        self.log.setGeometry(170, 100, 280, 290)
        self.log.setReadOnly(True)

        self.start_window = start_window
        self.saving_options_window = saving_options_window
        self.selected_isomers = selected_isomers
        self.inner_alkynes_specification = inner_alkynes_specification
        self.Lipinski_descriptors = Lipinski_descriptors
        self.Ghose_descriptors = Ghose_descriptors
        self.Veber_descriptors = Veber_descriptors
        self.Egan_descriptors = Egan_descriptors
        self.QED_descriptors = QED_descriptors
        self.Muegge_descriptors = Muegge_descriptors
        self.Leadlikeness_descriptors = Leadlikeness_descriptors
        self.logBB_model = logBB_model
        self.threshold = threshold
        self.saving_format = saving_format

        self.clear_log()
        self.show_log('Chosen generation parameters:\n\n')
        self.process()

    def process(self):
        if self.selected_isomers == '1_4':
            self.show_log('1,4-isomers are generated.\n')
        elif self.selected_isomers == '1_5':
            self.show_log('1,5-isomers are generated.\n')
        else:
            self.show_log('Both 1,5- and 1,4-isomers are generated.\n')

        if self.inner_alkynes_specification == 'ignore':
            self.show_log('Products for internal alkynes are omitted.\n')
        else:
            self.show_log('Products for internal alkynes are kept.\n')

        Lipinski_descriptors = ''
        if self.Lipinski_descriptors['donors']:
            Lipinski_descriptors += '\n-HDonors'
        if self.Lipinski_descriptors['acceptors']:
            Lipinski_descriptors += '\n-HAcceptors'
        if self.Lipinski_descriptors['weight']:
            Lipinski_descriptors += '\n-Molecular weight'
        if self.Lipinski_descriptors['logP']:
            Lipinski_descriptors += '\n-logP'
        if not self.Lipinski_descriptors['donors'] and not self.Lipinski_descriptors['acceptors'] \
                and not self.Lipinski_descriptors['weight'] and not self.Lipinski_descriptors['logP']:
            Lipinski_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Lipinski rules: {Lipinski_descriptors}.\n\n')

        Ghose_descriptors = ''
        if self.Ghose_descriptors['molecular_weight']:
            Ghose_descriptors += '\n-Molecular weight'
        if self.Ghose_descriptors['logP']:
            Ghose_descriptors += '\n-logP'
        if self.Ghose_descriptors['molar_refractivity']:
            Ghose_descriptors += '\n-Molar refractivity'
        if self.Ghose_descriptors['atoms_number']:
            Ghose_descriptors += '\n-Number of atoms'
        if not self.Ghose_descriptors['molecular_weight'] and not self.Ghose_descriptors['logP'] \
                and not self.Ghose_descriptors['molar_refractivity'] and not self.Ghose_descriptors['atoms_number']:
            Ghose_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Ghose rules: {Ghose_descriptors}.\n\n')

        Veber_descriptors = ''
        if self.Veber_descriptors['rotable_bonds']:
            Veber_descriptors += '\n-Rotable bonds'
        if self.Veber_descriptors['TPSA']:
            Veber_descriptors += '\n-TPSA'
        if not self.Veber_descriptors['rotable_bonds'] and not self.Veber_descriptors['TPSA']:
            Veber_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Veber rules: {Veber_descriptors}.\n\n')

        Egan_descriptors = ''
        if self.Egan_descriptors['logP']:
            Egan_descriptors += '\n-logP'
        if self.Egan_descriptors['TPSA']:
            Egan_descriptors += '\n-TPSA'
        if not self.Egan_descriptors['logP'] and not self.Egan_descriptors['TPSA']:
            Egan_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Egan rules: {Egan_descriptors}.\n\n')

        QED_descriptors = ''
        if self.QED_descriptors['molecular_weight']:
            QED_descriptors += '\n-Molecular weight'
        if self.QED_descriptors['rings_number']:
            QED_descriptors += '\n-Rings number'
        if self.QED_descriptors['rotable_bonds']:
            QED_descriptors += '\n-Rotable bonds'
        if self.QED_descriptors['donors']:
            QED_descriptors += '\n-HDonors'
        if self.QED_descriptors['acceptors']:
            QED_descriptors += '\n-HAcceptors'
        if self.QED_descriptors['logP']:
            QED_descriptors += '\n-logP'
        if not self.QED_descriptors['molecular_weight'] and not self.QED_descriptors['rings_number'] and not \
                self.QED_descriptors['rotable_bonds'] and not self.QED_descriptors['donors'] and not \
                self.QED_descriptors['acceptors'] and not self.QED_descriptors['logP']:
            QED_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to QED rules: {QED_descriptors}.\n\n')

        Muegge_descriptors = ''
        if self.Muegge_descriptors['molecular_weight']:
            Muegge_descriptors += '\n-Molecular weight'
        if self.Muegge_descriptors['logP']:
            Muegge_descriptors += '\n-logP'
        if self.Muegge_descriptors['TPSA']:
            Muegge_descriptors += '\n-TPSA'
        if self.Muegge_descriptors['rings_number']:
            Muegge_descriptors += '\n-Rings number'
        if self.Muegge_descriptors['carbon_atoms']:
            Muegge_descriptors += '\n-Carbon atoms number'
        if self.Muegge_descriptors['heteroatoms']:
            Muegge_descriptors += '\n-Heteroatoms number'
        if self.Muegge_descriptors['rotable_bonds']:
            Muegge_descriptors += '\n-Rotable bonds'
        if self.Muegge_descriptors['donors']:
            Muegge_descriptors += '\n-HDonors'
        if self.Muegge_descriptors['acceptors']:
            Muegge_descriptors += '\n-HAcceptors'
        if not self.Muegge_descriptors['molecular_weight'] and not self.Muegge_descriptors[
            'logP'] and not self.Muegge_descriptors['TPSA'] and not self.Muegge_descriptors[
            'rings_number'] and not self.Muegge_descriptors['carbon_atoms'] and not self.Muegge_descriptors[
            'heteroatoms'] and not self.Muegge_descriptors['rotable_bonds'] and not self.Muegge_descriptors[
            'donors'] and not self.Muegge_descriptors['acceptors']:
            Muegge_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Muegge rules: {Muegge_descriptors}.\n\n')

        Leadlikeness_descriptors = ''
        if self.Leadlikeness_descriptors['molecular_weight']:
            Leadlikeness_descriptors += '\n-Molecular weight'
        if self.Leadlikeness_descriptors['logP']:
            Leadlikeness_descriptors += '\n-logP'
        if self.Leadlikeness_descriptors['rotable_bonds']:
            Leadlikeness_descriptors += '\n-Rotable bonds'
        if not self.Leadlikeness_descriptors['rotable_bonds'] and not self.Leadlikeness_descriptors['logP'] and not \
                self.Leadlikeness_descriptors['molecular_weight']:
            Leadlikeness_descriptors += '\n-None'

        self.show_log(f'Molecules are filtered according to Leadlikeness rules: {Leadlikeness_descriptors}.\n\n')

        if self.logBB_model == 'Clark':
            self.show_log('LogBB Clark will be calculated.\n')
        else:
            self.show_log('LogBB Rishton will be calculated.\n')

        try:
            self.threshold = float(self.threshold)
            self.show_log(f'Molecules with logBB  less than {self.threshold} will be dropped.\n')
        except ValueError:
            self.show_log(f'Molecules with logBB  less than 0.3 will be dropped.\n\n')
            self.show_log(f'Warning: chosen threshold value {self.threshold} is invalid, so threshold is set to 0.3.\n')
            self.threshold = 0.3

        if self.saving_format == 'txt':
            self.show_log('An output file will be saved in .txt format.\n')
        else:
            self.show_log('An output file will be saved in .csv format.\n')

        self.activate_next()

    def clear_log(self):
        with open('parameters_log.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('parameters_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('parameters_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.saving_options_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.calculations_window = calculations.CalculationsWindow(self.start_window, self, self.selected_isomers,
                                                                   self.inner_alkynes_specification,
                                                                   self.Lipinski_descriptors, self.Ghose_descriptors,
                                                                   self.Veber_descriptors,
                                                                   self.Egan_descriptors, self.QED_descriptors,
                                                                   self.Muegge_descriptors,
                                                                   self.Leadlikeness_descriptors, self.logBB_model,
                                                                   self.threshold, self.saving_format)
        self.calculations_window.show()
