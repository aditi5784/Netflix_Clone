from flask import Flask, render_template, request
import numpy as np
import joblib
import csv
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/diabetes_model.pkl")

# Path for CSV file
csv_file = "data/predictions.csv"

# Ensure CSV exists with proper headers
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Risk", "Advice"
        ])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get form input as floats
    input_data = [float(x) for x in request.form.values()]
    final_input = np.array(input_data).reshape(1, -1)

    # Predict risk
    prediction = model.predict(final_input)[0]
    risk = "High" if prediction == 1 else "Low"

    # Unpack features for clarity
    pregnancies, glucose, bp, skin, insulin, bmi, dpf, age = input_data

    # Generate agentic advice
    advice = ""

    if risk == "High":
        advice += "⚠️ Your diabetes risk appears **high**. Let's break it down:\n\n"

        # Custom checks
        if glucose > 140:
            advice += f"• Your glucose level ({glucose}) is above normal. Try to limit sugary drinks, refined carbs, and sweets.\n"
        if bmi > 30:
            advice += f"• Your BMI ({bmi}) indicates obesity. Aim for gradual weight loss through 30 mins of brisk walking daily.\n"
        if bp > 130:
            advice += f"• Your blood pressure ({bp}) is on the higher side. Reduce salt and processed foods.\n"
        if insulin > 200:
            advice += f"• High insulin levels ({insulin}) may mean insulin resistance. Include more fiber (like oats, salads, fruits).\n"

        # General high-risk advice
        advice += (
            "\n🩺 **General Tips:**\n"
            "- Get a full medical checkup soon.\n"
            "- Follow a balanced diet (more greens, fewer carbs).\n"
            "- Track your fasting sugar weekly.\n"
            "- Manage stress with yoga or meditation.\n"
            "- Drink plenty of water.\n"
        )

    else:
        advice += "✅ Your diabetes risk appears **low** — great job maintaining your health!\n\n"
        advice += (
            "🌿 **Keep it up:**\n"
            "- Continue eating balanced meals.\n"
            "- Stay active at least 30 mins daily.\n"
            "- Drink enough water and get proper sleep.\n"
            "- Avoid excessive sugar to stay in this safe zone.\n"
            "- Go for annual checkups even if you feel fine.\n"
        )

    # Append prediction + advice to CSV
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(input_data + [risk, advice])

    # Display on frontend
    return render_template(
        "index.html",
        prediction_text=f"Risk Level: {risk}",
        advice=advice.replace("\n", "<br>")
    )


if __name__ == "__main__":
    app.run(debug=True)
