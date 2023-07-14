import numpy as np
import json
from scipy.spatial.transform import Rotation
data = {}
# Input coordinates
#Read Data
with open('./mediaPipeRes.json', "r") as json_data:
    data = json.loads(json_data.read())
#loop through data
for d in data:
    for key,val in d.items():
        # print(val)
        if key != "timeStamp":
                # print(val)
                rotation_matrix = Rotation.from_euler('xyz', [val['x'],val['y'], val['z']], degrees=True).as_matrix()
                angle_x = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])
                angle_y = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1]**2 + rotation_matrix[2, 2]**2))
                angle_z = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
                print(np.degrees(angle_x) ,np.degrees(angle_y) , np.degrees(angle_z))
      
# Create a rotation matrix

# Print the rotation matrix