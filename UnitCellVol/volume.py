import pandas as pd
import numpy as np

atoms = pd.read_csv("test_volume.csv") ##enter the file name here
radius = pd.read_csv("radius.csv") ##need to have a .csv file with radii stored.

a = atoms['unit_cell_formula'].to_dict()
a1 = str(a)
a2 = a1.replace('"', "")
atom_dict = eval(a2)

r = radius.set_index('symbol').T.to_dict('list')
r1 = str(r)
r2 = r1.replace("[", "").replace("]", "")
radius_dict = eval(r2)
k=0

for key in radius_dict.keys():
    for i in atom_dict.values():
        for j in i.keys():
            if key == j:   
                atom_dict[k][j] = (((4/3)*np.pi*(radius_dict[key]) ** 3) * (atom_dict[k][j]))
        k = k + 1
    k=0

tvol_list = []

for i in atom_dict.values():
    atom_list = list(i.values())
    atom_array = np.array(atom_list)
    total_volume = tvol_list.append(sum(atom_array))

tvol_df = pd.Series(tvol_list)
atoms = atoms.assign(volume_of_structure=tvol_df.values) 

vv = atoms['volume'].subtract(atoms['volume_of_structure'])
vv_df = pd.Series(vv)
atoms = atoms.assign(vacant_volume=vv_df.values)  
atoms.to_csv('vacant_volume.csv', encoding='utf-8', index=False)