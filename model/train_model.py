import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

np.random.seed(42)

records = 150

hours_studied = np.random.randint(1, 11, records)
attendance = np.random.randint(45, 96, records)
previous_score = np.random.randint(35, 91, records)

final_score = (
    0.4 * previous_score +
    0.3 * hours_studied * 5 +
    0.3 * attendance * 0.5 +
    np.random.randint(-5, 6, records)
)

df = pd.DataFrame({
    "hours_studied": hours_studied,
    "attendance": attendance,
    "previous_score": previous_score,
    "final_score": final_score
})

X = df[["hours_studied", "attendance", "previous_score"]]
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model R2 Score:", round(model.score(X_test, y_test), 3))

model_path = os.path.join(os.path.dirname(__file__), "student_model.pkl")
pickle.dump(model, open(model_path, "wb"))

print("Model saved successfully.")