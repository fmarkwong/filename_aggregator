#!/usr/local/bin/python3

import os
import ntpath
import csv

# filename_aggregator.py
# 
# Author: Mark Wong
#
# Compiles a list of all files in the current directory (including subdirectories)
# and outputs a CSV file of the list of full path filenames and aliases.
# An alias is the base filename without the extension.
#
# When script is run repeatedly, any new files will be added to the output.csv file while avoiding 
# duplicates.
#
# Usage:
#
#     - cd to desired directory
#     - python3 filename_aggregator.py


OUTPUT_CSV_FILENAME = 'output.csv'

def csv_filenames():
    csv_filenames = []
    if os.path.isfile(OUTPUT_CSV_FILENAME):
        with open(OUTPUT_CSV_FILENAME) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                  csv_filenames.append(row['FileName'])
    return csv_filenames

def all_current_filenames():
   all_current_filenames = []
   directory = os.getcwd()

   for dirpath, dirs, filenames in os.walk(directory):
       for filename in filenames:
           dirs[:] = [d for d in dirs if not d[0] == '.'] #https://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
           if filename[0] != '.' and filename not in [OUTPUT_CSV_FILENAME, os.path.basename(__file__)]:
               all_current_filenames.append(os.path.abspath(os.path.join(dirpath, filename)))
   return all_current_filenames

def alias(file_name):
    alias = ntpath.basename(file_name)
    alias = list(os.path.splitext(alias))[:-1]
    alias = ''.join(alias)
    return alias

def write_to_csv_file(file_names):
    with open(OUTPUT_CSV_FILENAME, 'w') as f:
        f.write("{},{}\n".format('FileName', 'Alias'))
        for file_name in file_names:
            f.write("{},{}\n".format(file_name, alias(file_name)))

merged_file_names = sorted(list(set(csv_filenames() + all_current_filenames())), key=str.lower)

write_to_csv_file(merged_file_names)
