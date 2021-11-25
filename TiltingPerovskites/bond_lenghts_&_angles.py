## Need to download the molmod library from: https://molmod.github.io/molmod/ to run this script ##


from __future__ import print_function
import numpy as np
import molmod as mm

mol = mm.Molecule.from_file('crystals.xyz') ## enter the .xyz file here.
angstorm = 1.889726133921252
deg = 0.0174533

assert(mol.graph is None)
mol.set_default_graph()

bonds = []
for b1 in range(mol.size):
    n = list(mol.graph.neighbors[b1])
    for index, b0 in enumerate(n):
        for b2 in n[:index]:
            bonds.append((b0, b1, b2))
print("An overview of all bonds:")
for b0, b1, b2 in bonds:
    bond = mm.ic.bond_length(mol.coordinates[[b0, b1, b2]])[0]
    print("%2i %2i %2i    %2s %2s %2s    %5.1f" % (
        b0, b1, b2, mol.symbols[b0], mol.symbols[b1], mol.symbols[b2], bond/angstorm
    ))

angles = []
for i1 in range(mol.size):
    n = list(mol.graph.neighbors[i1])
    for index, i0 in enumerate(n):
        for i2 in n [:index]:
            angles.append((i0, i1, i2))
print("An Overview of all bending angles in Lead Iodide:")
for i0, i1, i2 in angles:
    angle = mm.ic.bend_angle(mol.coordinates[[i0, i1, i2]])[0]
    print("%2i %2i %2i    %2s %2s %2s    %5.1f" % (
        i0, i1, i2, mol.symbols[i0], mol.symbols[i1], mol.symbols[i2], angle/deg
    ))