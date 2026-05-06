from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load files
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
symptoms_list = joblib.load("symptoms.pkl")

@app.route("/")
def home():
    return "Medical AI Chatbot Running"

# 🔍 NEW: Symptom suggestion API
@app.route("/symptoms", methods=["GET"])
def get_symptoms():
    query = request.args.get("q", "").lower()
    matches = [s for s in symptoms_list if query in s][:5]
    return jsonify(matches)

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json["symptoms"]

    if not isinstance(user_input, list):
        return jsonify({"error": "Symptoms must be a list"})

    user_input = [s.lower().strip().replace(" ", "_") for s in user_input]

    valid_symptoms = []
    for user_symptom in user_input:
        for known_symptom in symptoms_list:
            if user_symptom in known_symptom:
                valid_symptoms.append(known_symptom)

    valid_symptoms = list(set(valid_symptoms))

    if not valid_symptoms:
        return jsonify({
            "error": "Symptoms not recognized. Try typing slowly and selecting from suggestions."
        })

    input_vector = [0] * len(symptoms_list)

    for symptom in valid_symptoms:
        index = symptoms_list.index(symptom)
        input_vector[index] = 1

    input_df = pd.DataFrame([input_vector], columns=symptoms_list)

    prediction = model.predict(input_df)
    disease = label_encoder.inverse_transform(prediction)

    probs = model.predict_proba(input_df)
    confidence = max(probs[0]) * 100

    explanation = (
        f"The system predicts {disease[0]} based on symptoms: "
        f"{', '.join(valid_symptoms)}"
    )

    return jsonify({
        "prediction": disease[0],
        "confidence": f"{confidence:.2f}%",
        "explanation": explanation
    })

if __name__ == "__main__":
    app.run(debug=True)