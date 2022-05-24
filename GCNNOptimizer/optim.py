import os, shutil, glob 
import re
import numpy as np
from itertools import chain

s_path = '/home/akshay/Desktop/100_cifs/mp-1069.cif'
folder_path = '/home/akshay/Desktop/100_cifs/100_copies_1/'

### Input parameters for the function: number of copies required, dv = dropout value (needs to be between 0 and 1)


def cif_clones(num_of_copies, dv, lim_a, lim_b):
    for cif in range(1, num_of_copies + 1):
        filename = 1 * cif
        for ext in range (cif):
            flname_ext = 'mp-' + str(filename) + '.cif'
        d_path = folder_path + flname_ext
        copies = shutil.copy(s_path, d_path)

    for filename in glob.glob(os.path.join(folder_path, '*.cif')):
        with open(filename, "r") as cif_file:
            list_of_lines = cif_file.readlines()
            lol_list = list_of_lines[26:]
            lol_string = ''.join(lol_list)
            coordinates = re.findall(r'\d.\d\d\d\d\d\d\d\d',lol_string)
            row = len(coordinates)//3

            coord_arr = np.asarray(coordinates, dtype=np.float64).reshape(row, 3)
            rnge = (abs(lim_a) + lim_b)/2
            random_arr = rnge*np.random.randn(*coord_arr.shape)
            random_arr = np.clip(random_arr, lim_a, lim_b)
            random_arr *= np.random.binomial(1, dv, random_arr.shape)
            summ = np.add(coord_arr, random_arr)
            round_sum = np.round(summ, 7)
            sum_lol = round_sum.tolist()

            elements = re.findall(r'\w{1,2}\s\s\w{1,2}\d{1,2}\s\s\d', lol_string)
            ones = re.findall(r'\s\s\d$', lol_string)

            joined_list = list(chain.from_iterable(zip(elements, sum_lol)))
            for el in joined_list:
                el2 = []
                if type(el) == list:
                    for lst in el:
                        snum = '{:<011}'.format(str(lst))
                        el2.append(snum)
                    el.clear()
                    el.extend(el2)
            coords = str(joined_list).replace("['", " ").replace("[", "  ").replace("'", "")\
                        .replace("],", "  1\n").replace(",", "").replace("]]", "  1")  
            list_of_lines[26:] = coords
        with open(filename, "w") as cif_file:
            cif_file.writelines(list_of_lines)
            cif_file.close()
    return copies


function = cif_clones(10, 1, -0.05, 0.05)
print(function)
