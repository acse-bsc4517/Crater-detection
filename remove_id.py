import os
from tqdm import tqdm
import argparse

def remove_id(labels: str):
    new_label = ''
    for label in labels.splitlines():
        c, x, y, w, h = label.split(' ')[:5]
        new_label += ' '.join((c, x, y, w, h))
        new_label += '\n'
    return new_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type = str, default='.', help = 'path to dataset directory')
    arg = parser.parse_args()

label_path = arg.dir + os.sep + 'labels' + os.sep

filenames = [name[:-4] for name in os.listdir(label_path) if name.endswith('txt')]

for filename in tqdm(filenames):
    # reading file contents
    label_file = open(label_path + filename + '.txt', 'r')
    old_label = label_file.read()
    label_file.close()

    # writing file contents
    new_label = remove_id(old_label)
    label_file = open(label_path + filename + '.txt', 'w')
    label_file.write(new_label)
    label_file.close()


