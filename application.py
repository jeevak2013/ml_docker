import os
import sys
from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging
from src.exception import CustomException

application = Flask(__name__)
app = application

@app.route('/')
def index():
    # Renders the home landing page
    return render_template('index.html', results=None)

@app.route('/predict_datapoint', methods=['POST'])
def predict_datapoint():
    try:
        logging.info("Incoming prediction request received via Web Form")
        
        form_inputs = {
            'gender': request.form.get('gender'),
            'race_ethnicity': request.form.get('race_ethnicity'),
            'parental_level_of_education': request.form.get('parental_level_of_education'),
            'lunch': request.form.get('lunch'),
            'test_preparation_course': request.form.get('test_preparation_course'),
            'reading_score': request.form.get('reading_score'),
            'writing_score': request.form.get('writing_score')
        }
        
        custom_data_instance = CustomData(
            gender=form_inputs['gender'],
            race_ethnicity=form_inputs['race_ethnicity'],
            parental_level_of_education=form_inputs['parental_level_of_education'],
            lunch=form_inputs['lunch'],
            test_preparation_course=form_inputs['test_preparation_course'],
            reading_score=int(form_inputs['reading_score']),
            writing_score=int(form_inputs['writing_score'])
        )

        # Step 2: Convert the structured data object into a Pandas DataFrame format
        input_dataframe = custom_data_instance.get_data_as_dataframe()
        logging.info(f"Input features mapped to DataFrame successfully:\n{input_dataframe}")

        # Step 3: Instantiate prediction pipeline and execute preprocessing + scoring
        predict_pipeline = PredictPipeline()
        prediction_output = predict_pipeline.predict(features=input_dataframe)
        
        # Round the final math score output to 2 decimal places for user presentation
        final_result = round(prediction_output[0], 2)
        logging.info(f"Prediction success. Predicted Maths Score: {final_result}")

        # Step 4: Return result straight back onto your template UI container
        return render_template('index.html', results=final_result, inputs =form_inputs)

    except Exception as e:
        logging.error("Exception occurred inside the Flask web application route controller")
        raise CustomException(e, sys)

if __name__ == "__main__":
    # Launching local Flask production server on Port 5000
    app.run(host='0.0.0.0', port=5000)
