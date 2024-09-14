keypoint_start = [
    9, 11, 13, 13, 13,
    8, 10, 12, 14, 14, 14,
    9, 21, 22, 23, 25, 27,
    22, 24, 26, 28
]

keypoint_end = [
    11, 13, 15, 17, 19,
    10, 12, 14, 16, 18, 20,
    10, 22, 23, 25, 27, 29,
    24, 26, 28, 30
]

pose_map = {"downdog": 0, "goddess": 1, "plank": 2, "tree": 3, "warrior2": 4}

bodypart_angle_dict = {
    # Elbow angles
    "left_elbow": [5, 7, 9],   # Left arm (Left shoulder, Left elbow, Left wrist)
    "right_elbow": [6, 8, 10], # Right arm (Right shoulder, Right elbow, Right wrist)

    # Knee angles
    "left_knee": [11, 13, 15],   # Left leg (Left hip, Left knee, Left ankle)
    "right_knee": [12, 14, 16],  # Right leg (Right hip, Right knee, Right ankle)

    # Hip angles
    "left_hip": [5, 11, 13],   # Left side (Left shoulder, Left hip, Left knee)
    "right_hip": [6, 12, 14],  # Right side (Right shoulder, Right hip, Right knee)

    # Shoulder angles
    "left_shoulder": [7, 5, 6],   # Left shoulder (Left elbow, Left shoulder, Right shoulder)
    "right_shoulder": [8, 6, 5],  # Right shoulder (Right elbow, Right shoulder, Left shoulder)

    # Torso angle
    "torso": [11, 0, 12],   # Torso alignment (Left hip, Nose, Right hip)

    # Neck angles
    "left_neck": [5, 0, 1],   # Left side (Left shoulder, Nose, Left eye)
    "right_neck": [6, 0, 2],  # Right side (Right shoulder, Nose, Right eye)
}



