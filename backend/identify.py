import numpy as np
import torch
from dataset import create_edge_index
from variables import keypoint_end, keypoint_start, bodypart_angle_dict
import pandas as pd
from calculate_avg_angle import calculate_angle_from_nodes_3d

index = ['left_elbow', 'right_elbow', 'left_knee', 'right_knee', 'left_hip', 'right_hip', 
         'left_shoulder', 'right_shoulder', 'torso', 'left_neck', 'right_neck']

def read_coords(coords_df):
    # for val in coords_df.iloc[-1]:
        # if val < 0.5:
        #     return
        
    coords_df = coords_df.iloc[:, :-1]
    coords_df.drop(coords_df.tail(2).index,inplace=True)
    return coords_df

def get_prediction(coords, model):
    
    model.eval()
    x = torch.tensor(np.array(coords).reshape(31, 3), dtype=torch.float32)
    with torch.no_grad():
        out = model(x, create_edge_index(keypoint_start, keypoint_end), torch.tensor([0]))
        predictions = out.argmax(dim=1).item()
    return (predictions) 

def get_angle_diff(prediction, coords):
    keypoints = {}
    angle_diff = {}

    for i, row in coords.iterrows():
        keypoints[i] = row[0:4]

    correct_angles = pd.read_csv("angles.csv")
    correct_angles.index = index
    for angle in bodypart_angle_dict:
        nodes = bodypart_angle_dict[angle]
        joint_angle = calculate_angle_from_nodes_3d(keypoints, nodes[0], nodes[1], nodes[2])
        angle_diff[angle] = joint_angle - correct_angles.loc[angle, str(prediction)]
    return (angle_diff)
