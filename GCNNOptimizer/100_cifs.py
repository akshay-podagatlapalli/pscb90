import os, shutil, glob 
import re
import numpy as np
from itertools import chain

s_path = '/home/akshay/Desktop/100_cifs/mp-9272.cif'

for cif in range(1, 6):
    filename = 1 * cif
    for ext in range (cif):
        flname_ext = str(filename) + '.cif'
    d_path = '/home/akshay/Desktop/100_cifs/100_copies/' + flname_ext
    shutil.copy(s_path, d_path)


folder_path = '/home/akshay/Desktop/100_cifs/100_copies/'

for filename in glob.glob(os.path.join(folder_path, '*.cif')):
    with open(filename, "r") as cif_file:
        list_of_lines = cif_file.readlines()
        lol_list = list_of_lines[26:]
        lol_string = ''.join(lol_list)
        coordinates = re.findall(r'\d.\d\d\d\d\d\d\d\d',lol_string)
        
        coord_arr = np.asarray(coordinates, dtype=np.float64).reshape(12, 3) 
        random_arr = np.random.randn(*coord_arr.shape)                
        sum = np.add(coord_arr, random_arr)
        sum_lol = sum.tolist()
        
        
        elements = re.findall(r'\w{1,2}\s\s\w{1,2}\d{1,2}\s\s', lol_string)
        
        joined_list = list(chain.from_iterable(zip(elements, sum_lol)))
        new_coords = str(joined_list).replace("[", "  ").replace("]", "\n").replace("'", " ").replace(",", " ")
        list_of_lines[26:] = new_coords
    with open(filename, "w") as cif_file:
        cif_file.writelines(list_of_lines)
        cif_file.close()