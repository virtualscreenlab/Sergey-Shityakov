import os

files_to_delete = ['good_reagent_1.txt', 'good_reagent_2.txt', 'output.txt', 'output.csv', 'products.txt', 'products.csv',
                   'reagent_1_log.txt', 'reagent_2_log.txt', 'products_log.txt', 'swissADME_log.txt', 'conversion_log.txt',
                   'parameters_log.txt', 'imgs_log.txt', 'log.txt', 'triazoles.png']


def deletion_cycle(start=0):
    for i in range(start, len(files_to_delete)):
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), files_to_delete[i])
            os.remove(path)
        except FileNotFoundError:
            pass


def delete_extra_files(mode='normal'):
    if mode == 'triazoles_only':
        deletion_cycle(12)
    else:
        deletion_cycle()
