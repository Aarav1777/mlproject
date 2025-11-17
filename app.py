from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import traceback
import os

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    """
    GET  -> show form (home.html) with no result
    POST -> collect inputs, run pipeline, round & clamp result, render page with final_score
    """
    if request.method == 'GET':
        # No prediction yet
        return render_template('home.html', results=None)

    try:
        # collect form values (use defaults or convert safely)
        # If reading/writing might be empty strings, handle that.
        reading_val = request.form.get('reading_score', '')
        writing_val = request.form.get('writing_score', '')

        # convert to float if provided, otherwise use 0.0 (or choose another sensible default)
        reading_score = float(reading_val) if reading_val not in (None, '', 'None') else 0.0
        writing_score = float(writing_val) if writing_val not in (None, '', 'None') else 0.0

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        print("Input dataframe for prediction:\n", pred_df)

        predict_pipeline = PredictPipeline()
        raw_results = predict_pipeline.predict(pred_df)  # usually returns array-like
        print("Raw model output:", raw_results)

        # Safely extract a scalar prediction
        # If raw_results is array-like (e.g. [100.1413]) or a single value
        if isinstance(raw_results, (list, tuple, np.ndarray)):
            pred_value = raw_results[0]
        else:
            pred_value = raw_results

        # Convert to float and ensure numeric
        pred_value = float(pred_value)

        # Round to 2 decimals and clamp between 0 and 100
        final_score = round(pred_value, 2)
        final_score = max(0.0, min(final_score, 100.0))

        # Optionally convert to int if you prefer whole numbers:
        # final_score = int(round(final_score))

        print("Final score (rounded & clamped):", final_score)

        return render_template('home.html', results=final_score)

    except Exception as e:
        # Log error and show friendly message on the page
        print("Prediction error:", str(e))
        traceback.print_exc()
        error_msg = "Error during prediction. Please check inputs."
        return render_template('home.html', results=error_msg)


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
