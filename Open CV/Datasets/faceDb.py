import cv2
import numpy as np
import pickle
from insightface.app import FaceAnalysis

# -----------------------------
# Load ArcFace model
# -----------------------------
app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))  # ctx_id=0 for CPU, use GPU id for CUDA

# -----------------------------
# Load Face Database
# -----------------------------
with open(r"C:\Users\suraj\OneDrive\Desktop\PYTHON1\face_db.pkl", "rb") as f:
    face_db = pickle.load(f)  # { "Name": [embedding1, embedding2, ...] }

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def recognize_face(embedding):
    best_match = "Unknown"
    best_score = -1
    threshold = 0.40  # Adjust based on tests

    for name, embeds in face_db.items():
        for db_embed in embeds:
            score = cosine_similarity(embedding, db_embed)
            if score > best_score:
                best_score = score
                best_match = name

    if best_score < threshold:
        best_match = "Unknown"
    return best_match, best_score

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)  # Detect multiple faces
    for face in faces:
        bbox = face.bbox.astype(int)
        embedding = face.embedding
        name, score = recognize_face(embedding)

        # Draw box
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({score:.2f})", (bbox[0], bbox[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("ArcFace Multi-Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
