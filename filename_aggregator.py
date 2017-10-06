# !/usr/local/bin/python3

import os
import ntpath
import csv

OUTPUT_CSV_FILENAME = 'output.csv'

def all_files(directory):
   for dirpath, dirs, filenames in os.walk(directory):
       for f in filenames:
           dirs[:] = [d for d in dirs if not d[0] == '.'] #https://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
           if f[0] != '.':
               yield os.path.abspath(os.path.join(dirpath, f))

csv_filenames = []

if os.path.isfile(OUTPUT_CSV_FILENAME):
    with open(OUTPUT_CSV_FILENAME) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
              csv_filenames.append(row['FileName'])


files = [file for file in all_files(os.getcwd())]

merged_files = sorted(list(set(csv_filenames + files)), key=str.lower)

with open(OUTPUT_CSV_FILENAME, 'w') as f:
    f.write("{},{}\n".format('FileName', 'Alias'))
    for file_name in merged_files:
        alias = ntpath.basename(file_name)
        alias = list(os.path.splitext(alias))[:-1]
        alias = ''.join(alias)
        f.write("{},{}\n".format(file_name, alias))

