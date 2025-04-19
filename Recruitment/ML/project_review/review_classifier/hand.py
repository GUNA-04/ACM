import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

x = pd.read_csv("C:\\Users\\techn\\Documents\\GitHub\\ACM\\Recruitment\\ML\\project_review\\hand_writing\\IMDB Dataset.csv")
print(x.head())
print(x.describe())
print(x.columns)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(x['review'])

y = x['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
