# Module that includes functions to extract numberical data
# from the dataset's labels files

import os

def get_data(directory: str):
  craterlist = []
  label_path = directory + os.sep + 'labels' + os.sep
  textfiles = [name for name in os.listdir(label_path) if 'v' not in name and 'h' not in name]

  for textfile in textfiles:
    file  = open(label_path + textfile, 'r')
    labels = file.read()
    file.close()

    sublist = []
    for label in labels.splitlines():
      x, y, w, h = [float(x) for x in label.split(' ')[1:5]]
      sublist.append([x, y, w, h])

    craterlist.append([sublist, textfile])
  return craterlist

def get_vals(data):
  countlist = []
  woh_list  = []
  xy_list   = []
  d_list    = []
  for i in range(len(data)):
    countlist.append(len(data[i][0]))
  
  for i in range(len(data)):
    for j in range(len(data[i][0])):
      woh_list.append(data[i][0][j][2] / data[i][0][j][3])
      xy_list.append(data[i][0][j][:2])
      d_list.append((data[i][0][j][2] + data[i][0][j][3])/2)
  return countlist, woh_list, xy_list, d_list
