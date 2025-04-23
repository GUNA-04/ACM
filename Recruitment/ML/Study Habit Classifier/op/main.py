from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample training data
X = np.array([
    [5, 8, 2, 0],
    [2, 3, 8, 2],
    [4, 6, 5, 1],
    [6, 9, 1, 0],
    [1, 2, 9, 2],
    [3, 5, 4, 1],
])
y = ["Consistent", "Inconsistent", "Needs Improvement", "Consistent", "Inconsistent", "Needs Improvement"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

class StudyData(BaseModel):
    hours: float
    focus: float
    distraction: float
    active: int

@app.post("/predict")
def predict(data: StudyData):
    features = np.array([[data.hours, data.focus, data.distraction, data.active]])
    prediction = model.predict(features)[0]
    return {"result": prediction}
