import os
import pickle
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image
import cv2

# Initialize ArcFace
app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# Path to dataset folder
DATASET_PATH = r"PYTHON-FULL\Open CV\Datasets"

face_db = {}

for person_name in os.listdir(DATASET_PATH):
    person_path = os.path.join(DATASET_PATH, person_name)
    if not os.path.isdir(person_path):
        continue

    embeddings = []
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        # Load image
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Detect face(s)
        faces = app.get(img)
        if len(faces) == 0:
            print(f"[WARNING] No face found in {img_path}")
            continue

        # Take the first detected face
        embedding = faces[0].embedding
        embeddings.append(embedding)

    if embeddings:
        face_db[person_name] = embeddings
        print(f"[INFO] Added {person_name} with {len(embeddings)} embeddings")

# Save database
with open("face_db.pkl", "wb") as f:
    pickle.dump(face_db, f)

print("[INFO] Face database saved to face_db.pkl")
