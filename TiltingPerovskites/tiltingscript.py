import os
import numpy as np
import molmod as mm
from molmod import ic as mmic
from molmod import io as mmio
from molmod import molecular_graphs


xr = mmio.xyz.XYZReader("crystals.xyz", file_unit=1.889726133921252)
xr.set_default_graph()

angles = []
for i1 in range (xr.size):
    n = list(xr.graph.neighbors[i1])
    for index, i0 in enumerate(n):
        for i2 in n[:index]:
            angles.append((i0, i1, i2))

print("An overview of all bending angles")
for i0, i1, i2 in angles:
    angle = mmic.bend_angle(xr.coordinates[[i0, i1, i2]])[0]
print("%2i %2i %2i    %2s %2s %2s    %5.1f" % (
        i0, i1, i2, xr.symbols[i0], xr.symbols[i1], xr.symbols[i2], angle/deg
    ))










