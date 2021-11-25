import glob
import os
import requests
import json

lanthanides_list = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
structure_id = []
mpid_list = []

folder_path = '/home/akshay/Desktop/Lanthanide Filter/cifs'    

def lanth_filter():  
  for filename in glob.glob(os.path.join(folder_path, '*.cif')):
    for lanthanide in lanthanides_list:
      with open(filename) as cif_file:    
        for line in cif_file.readlines():
          if lanthanide in line:
            structure_id.append(cif_file.name)

  result = ('\n'.join(map(str, structure_id)))

  with open("filtered_lanthanides.txt", 'w') as output:
    output.write(str(result))
  return

lanth_filter()

def olanth_filter(filename):
  with open(filename, 'r') as mp_ids:
    for mpid in mp_ids:
      mpid = mpid.strip()
      url = "https://www.materialsproject.org/rest/v2/materials/" + mpid + "/vasp?API_KEY=4RlBg415ibVMTPhPxbTf"
      r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
      response_dict = r.json()
      mat_info = response_dict['response']
      if len(mat_info) == 1: 
        smat_info = mat_info[0]
      for lanthanide in lanthanides_list:
        if lanthanide in smat_info['pretty_formula']:
          mpid_list.append(smat_info['material_id'])
  return print(mpid_list)  

olanth_filter(filename)