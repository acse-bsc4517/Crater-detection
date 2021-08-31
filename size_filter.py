# Running this file will filter out craters smaller than a user-specified threshold
# This will replace the original labels with a new set of filtered labels
# The original labels are saved in 'original_labels'
import os
from tqdm import tqdm
import argparse

def label_filter_size(labels: str, min_size: float, max_size: float):
    new_label = ''
    for label in labels.splitlines():
        c, x, y, w, h = label.split(' ')[:5]
        w_val = float(w)
        h_val = float(h)
        if (max_size > w_val >= min_size and max_size > h_val >= min_size):
            new_label += ' '.join((c, x, y, w, h))
            new_label += '\n'
    return new_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type = str, default='dataset_lunar', help='path to dataset directory')
    parser.add_argument('--min', type = int, default = 0, help='Size in pixels for crater width/height below which you want to filter out')
    parser.add_argument('--max', type = int, default = 593, help='Size in pixels for crater width/height above which you want to filter out')
    parser.add_argument('--img', type = int, default = 593, help = 'The size of image in pixels (assuming image is sqaure)')
    parser.add_argument('--revert', type = bool, default = False, help = 'Remove the (modified) label directory and recover original labels')
    arg = parser.parse_args()

# Checking if 'dir/original labels' exists
# if not, this assumes the current 'dir/labels' directory holds the original labels
somepath = arg.dir + os.sep + 'original_labels' + os.sep
original_saved = os.path.isdir(somepath)

if original_saved == False:
    os.system('mkdir ' + arg.dir + os.sep + 'original_labels')
    os.system('cp -r ' + arg.dir + os.sep +'labels/* ' + arg.dir + os.sep + 'original_labels')

os.system('rm -rf ' + arg.dir + os.sep + 'labels')
os.system('mkdir ' + arg.dir + os.sep + 'labels')
os.system('cp -r ' + arg.dir + os.sep + 'original_labels/* ' + arg.dir + os.sep + 'labels')

if arg.revert == True:
    os.system('rm -rf ' + arg.dir + os.sep + 'original_labels')

else:
    label_path = arg.dir + os.sep + 'labels' + os.sep

    filenames = [name[:-4] for name in os.listdir(label_path) if name.endswith('txt')]

    minimum = arg.min/arg.img
    maximum = arg.max/arg.img
    for filename in tqdm(filenames):
        label_file = open(label_path + filename + '.txt', 'r')
        old_label = label_file.read()
        label_file.close()

        new_label = label_filter_size(old_label, minimum, maximum)

        # If there are still craters remaining after filter -> overwrite file
        if len(new_label) != 0:
            label_file = open(label_path + filename + '.txt', 'w')
            label_file.write(new_label)
            label_file.close()
        # If no crater remains after filtering -> delete file
        else:
            os.system('rm ' + label_path + filename + '.txt')
    