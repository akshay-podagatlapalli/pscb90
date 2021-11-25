from __future__ import print_function
import numpy as np
import molmod as mm

mol = mm.Molecule.from_file('crystals.xyz')
angstorm = 1.889726133921252
deg = 0.0174533

assert(mol.graph is None)
mol.set_default_graph()

angle = np.degrees(34.1)

a = float(10.1342) 
b = float(12.0883)
c = float(13.4606) 


r_x = np.ndarray([[1, 0,              0            ],
                  [0, np.cos(angle), -np.sin(angle)],
                  [0, np.sin(angle), np.cos(angle) ]
                  ])
r_y = np.ndarray([[np.cos(angle), 0, np.sin(angle) ],
                  [0,             1, 0             ],
                  [-np.sin(angle), 0, np.cos(angle)]
                  ])
r_z = np.ndarray([[np.cos(angle), -np.sin(angle), 0],
                 [np.sin(angle), np.cos(angle),   0],
                 [0,             0,               1]
                 ])


mm.transformations.Rotation(r_x)
#mm.transformations.Rotation(r_y)
#mm.transformations.Rotation(r_z)

vector_rotated = np.array([a, b, c])
x = vector_rotated
mm.transformations.Rotation.apply_to(x)


print(vector_rotated)

    