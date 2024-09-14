import mediapipe as mp
import cv2
from paths import IMG_TRAIN_DIR, IMG_TEST_DIR

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

train_data, test_data = [], []
for directory in IMG_TRAIN_DIR.iterdir():
    yoga_type = directory.name
    for image_path in directory.iterdir():
        image = cv2.imread(image_path)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        landmarks = pose.process(image_rgb).pose_landmarks

        if landmarks is None: continue

        keypoints = [(landmark.x, landmark.y, landmark.z) for landmark in landmarks.landmark]
        
        row = {}

        for i in range(len(keypoints)):
            row[f'x_{i}'] = keypoints[i][0]
            row[f'y_{i}'] = keypoints[i][1]
            row[f'z_{i}'] = keypoints[i][2]

        row['pose'] = yoga_type
        train_data.append(row)

for directory in IMG_TEST_DIR.iterdir():
    yoga_type = directory.name
    for image_path in directory.iterdir():
        image = cv2.imread(image_path)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        landmarks = pose.process(image_rgb).pose_landmarks

        if landmarks is None: continue

        keypoints = [(landmark.x, landmark.y, landmark.z) for landmark in landmarks.landmark]
        
        row = {}

        for i in range(len(keypoints)):
            row[f'x_{i}'] = keypoints[i][0]
            row[f'y_{i}'] = keypoints[i][1]
            row[f'z_{i}'] = keypoints[i][2]

        row['pose'] = yoga_type
        train_data.append(row)