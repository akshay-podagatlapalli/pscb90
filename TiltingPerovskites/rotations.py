import numpy as np
import scipy as scipy
from scipy import spatial

x = float(6.7684) 
y = float(9.9854)
z = float(11.1644)

vector = [x, y, z]

rotation_axis = np.array([0, 1, 1])
rotvec = rotation_axis

scipy.spatial.transform.Rotation.from_rotvec(rotvec)

rotation_degrees = np.degrees(180)

rotation_radians = np.degrees(rotation_degrees)

rotation_vector = rotation_radians * rotation_axis
rotation = scipy.spatial.transform.Rotation.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(vector)


print(rotated_vec)