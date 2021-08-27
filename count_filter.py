import os
from tqdm import tqdm
import argparse
from data_extract import *

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type = str, default='dataset_lunar', help='path to dataset directory')
    parser.add_argument('--min', type = int, default = 0, help=' ')
    parser.add_argument('--max', type = int, default = 100, help='')
    parser.add_argument('--revert', type = bool, default = False, help = 'Remove the (modified) label directory and recover original labels')
    arg = parser.parse_args()

min_count = arg.min
max_count = arg.max
string = ''

data = get_data(arg.dir)
vals = get_vals(data)

for i, x in enumerate(vals[0]):
    if (x >= min_count and x < max_count):
        string += '../dataset_lunar/images/' + data[i][1][:-4] + '.png\n'

f = open(arg.dir + os.sep + 'test.txt', 'w')
f.write(string)
f.close()
