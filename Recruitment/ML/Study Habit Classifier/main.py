from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


X = np.array([
    [5, 8, 2, 0],
    [2, 3, 8, 2],
    [4, 6, 5, 1],
    [6, 9, 1, 0],
    [1, 2, 9, 2],
    [3, 5, 4, 1],
])
y = ["Consistent", "Inconsistent", "Needs Improvement", "Consistent", "Inconsistent", "Needs Improvement"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


class StudyData(BaseModel):
    hours: float
    focus: float
    distraction: float
    active: int

@app.post("/predict")
def predict(data: StudyData):
    features = np.array([[data.hours, data.focus, data.distraction, data.active]])
    prediction = model.predict(features)[0]
    return {"result": prediction, "accuracy": accuracy}
