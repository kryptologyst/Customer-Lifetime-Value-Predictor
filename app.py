import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('clv_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from the form
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Predict CLV
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text=f'Predicted Customer Lifetime Value: ${output}')

if __name__ == "__main__":
    app.run(debug=True)
