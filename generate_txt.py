# Generate train.txt, valid.txt and test.txt that can be read by YOLO data yaml files
import argparse
import os
import random
import math
import platform

slash = "/"
if platform.system().lower() == 'windows':
    slash = "\\"

random.seed(0)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='dataset', help='The directory that encloses the dataset, or where the images and label directory resides')
    parser.add_argument('--train', type=float, default=0.7, help='fraction of the dataset that will be used for training')
    parser.add_argument('--val', type=float, default=0.2, help='fraction of the dataset that will be used for validation')
    parser.add_argument('--test', type=float, default=0.1, help='fraction of the dataset that will be used for testing')
    parser.add_argument('--size', type = int, default = 20000, help='number of images to use as dataset, e.g. if size=10, only 10 data from the dataset will be used')
    arg = parser.parse_args()

txt_files = []
os.chdir(os.path.join(arg.dir, "labels"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        txt_files.append("../" + arg.dir + "/images/" + filename[:-4] + ".png")
os.chdir("..")

if arg.size >= len(txt_files):
  n = len(txt_files)
else:
  n = arg.size

s = arg.train + arg.val + arg.test
a = math.floor(n*arg.train/s)
b = math.ceil(n*arg.val/s)
c = s - a - b

# Randomly shuffle the names and distribute it across training, validation and testing
random.shuffle(txt_files)
trainlist = txt_files[0:a]
vallist = txt_files[a:b+a]
testlist = txt_files[b+a:n]

print('Total number of images considered = %i' %n)
print('The number of images for')
print('training = %i' %len(trainlist))
print('validation = %i' %len(vallist))
print('testing = %i' %len(testlist))

# Write files
if len(trainlist) != 0:
    f = open("train.txt","w")
    for stuff in trainlist:
        f.write(stuff)
        f.write("\n")
    f.close

if len(vallist) != 0:
    f = open("valid.txt","w")
    for stuff in vallist:
        f.write(stuff)
        f.write("\n")
    f.close

if len(testlist) != 0:
    f = open("test.txt","w")
    for stuff in testlist:
        f.write(stuff)
        f.write("\n")
    f.close