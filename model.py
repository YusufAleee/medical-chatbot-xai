import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("../dataset/dataset.csv")

# Fill missing values
data = data.fillna("None")

# -----------------------------
# GET ALL UNIQUE SYMPTOMS
# -----------------------------
symptom_columns = data.columns[1:]  # skip Disease column

all_symptoms = set()

for col in symptom_columns:
    all_symptoms.update(data[col].unique())

all_symptoms.discard("None")  # remove empty

all_symptoms = list(all_symptoms)

# -----------------------------
# CREATE NEW FEATURE MATRIX
# -----------------------------
X = []

for index, row in data.iterrows():
    row_symptoms = row[symptom_columns].values
    row_vector = [1 if symptom in row_symptoms else 0 for symptom in all_symptoms]
    X.append(row_vector)

X = pd.DataFrame(X, columns=all_symptoms)

# -----------------------------
# ENCODE TARGET
# -----------------------------
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data["Disease"])

# -----------------------------
# TRAIN MODEL
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# -----------------------------
# SAVE EVERYTHING
# -----------------------------
joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(all_symptoms, "symptoms.pkl")

print("Model rebuilt with real symptoms!")