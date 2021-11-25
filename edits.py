import os, glob
import re
import numpy as np
from itertools import chain


folder_path = '/home/akshay/Desktop/100_cifs/100_copies/'

a = (r'\d.\d\d\d\d\d\d\d\d')*18

for filename in glob.glob(os.path.join(folder_path, '*.cif')):
    with open(filename, "r") as cif_file:
        list_of_lines = cif_file.readlines()
        lol_list = list_of_lines[26:]
        lol_string = ''.join(lol_list)
        coordinates = re.findall(r'\d.\d\d\d\d\d\d\d\d',lol_string)
        
        coord_arr = np.asarray(coordinates, dtype=np.float64).reshape(6, 3)
        random_arr = 0.1 * np.random.randn(*coord_arr.shape)
        sum = np.add(coord_arr, random_arr)
        sum_lol = sum.tolist()
        
        
        elements = re.findall(r'\w\w\s\s\w\w\d', lol_string)
        
        joined_list = list(chain.from_iterable(zip(elements, sum_lol)))
        new_coords = str(joined_list).replace("[", "  ").replace("]", "\n").replace("'", " ").replace(",", " ")
        print(new_coords)
            
        