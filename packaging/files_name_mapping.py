#!/usr/bin/python3
import re
import shutil
import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

mapping_list = {
    'X8R': ['X6R', 'X8R'],
    'RX4R': ['RX4R', 'RX6R'],
    'RXXR_GRXX': ['G-RX6', 'G-RX8'],
    'RX8RPRO': ['RX8R-PRO'],
}

raw_dir = os.path.normpath(f'{SCRIPT_DIR}/../raw/')
to_dir = os.path.normpath(f'{SCRIPT_DIR}/..')
frk_list = os.listdir(raw_dir)

for from_name in frk_list:
    to_name = from_name.lower()
    g = re.match('(uni_)?(.*)_([a-z]*)(\d{2,3})([a-z]*)\.frk', to_name)
    g1 = g.group(1)
    rx_name = g.group(2).upper()
    g3 = g.group(3)
    ver = g.group(4)
    g5 = g.group(5)

    g3 = g3.replace('rom', '')
    g5 = g5.replace('rom', '')
    postfix = g3 + g5

    if rx_name in mapping_list:
        mapped_rxs = mapping_list[rx_name]
        for mapped_rx in mapped_rxs:
            to_name = f'uni_{mapped_rx}_v{ver}{postfix}.frk'
            print(to_name)
            shutil.copy2(f'{raw_dir}/{from_name}', f'{to_dir}/{to_name}')
    else:
        to_name = f'uni_{rx_name}_v{ver}{postfix}.frk'
        print(to_name)
        shutil.copy2(f'{raw_dir}/{from_name}', f'{to_dir}/{to_name}')

    print(to_name)
    pass
