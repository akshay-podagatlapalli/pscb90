import requests
import json
import pymatgen.core.periodic_table as mg

lanthanides_list = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]

filename = "/home/akshay/Desktop/Lanthanide Filter/afile.csv"

mpid_list = []

with open(filename, 'r') as mp_ids:
  for mpid in mp_ids:
    mpid = mpid.strip()
    url = "https://www.materialsproject.org/rest/v2/materials/" + mpid + "/vasp?API_KEY=4RlBg415ibVMTPhPxbTf"
    r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    response_dict = r.json()
    mat_info = response_dict['response']
    if len(mat_info) == 1: 
      smat_info = mat_info[0]
      for el in smat_info['elements']:
        ele = mg.Element(el)
        if ele.is_transition_metal:
          print(smat_info['pretty_formula'])  