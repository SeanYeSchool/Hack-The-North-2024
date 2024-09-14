import numpy as np
from variables import bodypart_angle_dict, pose_map
from paths import IMG_TRAIN_DIR
import mediapipe as mp
import pandas as pd
import copy

def calculate_angle_from_nodes_3d(nodes, node_A, node_B, node_C):
    A = np.array(nodes[node_A])
    B = np.array(nodes[node_B])
    C = np.array(nodes[node_C])

    AB, BC = A-B, C-B

    dot_prod = np.dot(AB, BC)
    mag_AB = np.linalg.norm(AB)
    mag_BC = np.linalg.norm(BC)

    angle = dot_prod / (mag_AB * mag_BC)

    angle = np.clip(angle, -1, 1)

    angle = np.degrees(np.arccos(angle))
    return angle

def create_avg_angles():

    angle_dict = {"left_elbow": [], "right_elbow": [],
    "left_knee": [], "right_knee": [],
    "left_hip": [], "right_hip": [],
    "left_shoulder": [], "right_shoulder": [],
    "torso": [],
    "left_neck": [], "right_neck": []}

    angle_accum = {i: copy.deepcopy(angle_dict) for i in range(5)}

    train_df = pd.read_csv("TRAIN_DF.csv")

    for index, row in train_df.iterrows():
        yoga_type = row.iloc[-1]

        keypoints = {i: [] for i in range(31)}
        for i in range(31):
            keypoints[i] = row[i*3:(i*3)+3]
        for angle in bodypart_angle_dict:
            
            nodes = bodypart_angle_dict[angle]
            joint_angle = calculate_angle_from_nodes_3d(keypoints, nodes[0], nodes[1], nodes[2])

            angle_accum[pose_map[yoga_type]][angle].append(joint_angle)

    for yoga_index in angle_accum:
        for joint_angle in angle_accum[yoga_index]:
            angle_accum[yoga_index][joint_angle] = sum(angle_accum[yoga_index][joint_angle]) / 250


    df = pd.DataFrame(angle_accum)
    df.to_csv("angles.csv")