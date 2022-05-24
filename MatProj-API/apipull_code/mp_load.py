#!/usr/bin/env python3

import urllib.request
import json
import sys
import os.path
import argparse

APIKEY = "enter API KEY here" #API KEY const
PARAMLIST = ["energy", "energy_per_atom", "volume", "formation_energy_per_atom", "nsites", 
            "e_above_hull", "band_gap", "density",] #numeric parameters

def mpload(mpid, apikey): #dict mpload(str, str)
    URLBASE = "https://materialsproject.org/rest/v2/materials/{}/vasp?API_KEY={}"
    url = urllib.request.Request(URLBASE.format(mpid, apikey), headers = {'User-Agent':'Mozilla/5.0'})
    #print(url)
    return json.loads(urllib.request.urlopen(url).read())
    
def cif_dload(filename, params, apikey): #list cif_dload(str, list, str)
    itemset = []
    deads = []
    try:
        with open(filename, 'r') as mp_ids:
            for mpid in mp_ids:
                mpid = mpid.strip()
                try:
                    mp_item = mpload(mpid, apikey)["response"][0]
                    cifdata = mp_item["cif"]
                    if not os.path.isfile(mpid.split(".")[0] + ".cif"):
                        with open(mpid.split(".")[0] + ".cif", "w") as cifout:
                            cifout.write(cifdata)
                except IndexError:
                    print("No cif:", mpid)
                    deads.append(mpid)
                    continue
                except urllib.error.HTTPError:
                    print("Dead link: ", mpid)
                    deads.append(mpid)
                    continue
                buffer = []
                for param in params:
                    try:
                        buffer.append(str(mp_item[param]))
                    except KeyError:
                        buffer.append("None")
                print(mpid, buffer)
                itemset.append([mpid, *buffer])
                
    except FileNotFoundError:
        print("File not found")
    print("Dead links:")
    print(deads)
    return itemset

def main(argv): #int main(list)
    parser = argparse.ArgumentParser(description = "Downloads cif files from a list of mp-ids, generates a master csv with numeric properties", usage="%(prog)s id_list [options]")
    pgroup = parser.add_mutually_exclusive_group()
    parser.add_argument("id_list", type = str, help = "List of mp-ids, each on own line")
    pgroup.add_argument("-p", "--params", metavar = "P", nargs = "+", help = "List of parameters")
    pgroup.add_argument("-r", "--restrict", metavar = "R", nargs = "+", choices = PARAMLIST, help = "Restrict parameters from: " + ", ".join(PARAMLIST))
    parser.add_argument("-o", "--output", metavar = "Output", default="id_prop_master.csv", help = "Output file name (id_prop_master.csv)")
    parser.add_argument("-a", "--apikey", metavar = "Key", help = "Modify Materials Project API key (please set in source)")
    parser.add_argument("-H", "--header", action = "store_false", help = "Turn off headers in csv")
    argV = parser.parse_args(argv[1:])
    #set from constants
    if(argV.params):
        paramlist = argV.params
    elif(argV.restrict):
        paramlist = argV.restrict
    else:
        paramlist = PARAMLIST
    if(argV.apikey):
        apikey = argV.apikey
    else:
        apikey = APIKEY
    #file writing
    id_list = argV.id_list
    mp_list = cif_dload(id_list, paramlist, apikey)
    with open(argV.output, "w") as outfile:
        if(argV.header):
            outfile.write("id, " + ", ".join(paramlist) + "\n")
        for i in mp_list:
            outfile.write(", ".join(i) + "\n")
    return 0
    
if __name__ == "__main__":
    main(sys.argv)
