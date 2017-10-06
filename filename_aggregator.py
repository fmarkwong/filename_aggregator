import os
import ntpath
import csv

def all_files(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           if f[0] != '.':
               yield os.path.abspath(os.path.join(dirpath, f))

csv_filenames = []

if os.path.isfile('1output.csv'):
    with open('1output.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
              csv_filenames.append(row['FileName'])


files = [file for file in all_files(os.getcwd())]

merged_files = sorted(list(set(csv_filenames + files)), key=str.lower)

with open('1output.csv', 'w') as f:
    f.write("{},{}\n".format('FileName', 'Alias'))
    for file_name in merged_files:
        alias = ntpath.basename(file_name)
        alias = list(os.path.splitext(alias))[:-1]
        # alias.pop()
        alias = ''.join(alias)
        f.write("{},{}\n".format(file_name, alias))

