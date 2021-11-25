import numpy as np

a = np.array([[0.0, 0.0, 0.0  ],
              [-3.16, 0.0, 0.0    ], 
              [0.0, 3.16, 0.0 ], 
              [3.16, 0.0, 0.0  ], 
              [0.0, -3.16, 0.0],
              [0.0, 0.0, 3.16 ],
              [0.0, 0.0, -3.16]
              ])
T_a = a.transpose()
b = T_a[0] + ((3.16 * np.cos((1 * np.pi) / 12)) * 2)
#b = T_a[0] + 6.32

deg =  -15 ####CHANGE THIS VALUE####

def main(x, y, z):
    if deg >= 0:
        theta = (np.pi / 180) * deg
        p = np.array([0.0, 0.0, 0.0])
    elif deg <= 0:
        theta = (np.pi / 180) * (360 + deg)
        p = np.array([6.32, 0.0, 0.0])

    x_values = (x - p[0]) * np.cos(theta) - (y - p[1]) * np.sin(theta) + p[0]
    y_values = (x - p[0]) * np.sin(theta) + (y - p[1]) * np.cos(theta) + p[1]
    z_values = (x - p[0]) * np.sin(0) + (z - p[2]) * np.cos(0) + p[2]
    return np.array([x_values, y_values, z_values])

if deg >= 0:
    c_x = T_a[0] 
    c_y = T_a[1]
    c_z = T_a[2]
    result = main(c_x, c_y, c_z).transpose()

    with open('coordinates.xyz', 'w') as f:
        for item in result:
            f.write("%s\n" % item)

if deg <= 0:
    c_x = b 
    c_y = T_a[1]
    c_z = T_a[2]
    result = main(c_x, c_y, c_z).transpose()

    with open('coordinates.xyz', 'a') as f:
        for item in result:
            f.writelines("\n")
            f.write("%s" % item)    