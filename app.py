from flask import Flask, render_template, jsonify, request
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomData
from src.logger.logging import logging  # Assuming the logger is already set up in your src package

app = Flask(__name__)

@app.route('/')
def home_page():
    logging.info("Rendering the home page.")
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        logging.info("GET request received. Rendering form.html.")
        return render_template("form.html")
    else:
        try:
            logging.info("POST request received for prediction.")
            # Collecting input data from the form
            data = CustomData(
                carat=float(request.form.get("carat")),
                depth=float(request.form.get("depth")),
                table=float(request.form.get("table")),
                x=float(request.form.get("x")),
                y=float(request.form.get("y")),
                z=float(request.form.get("z")),
                cut=request.form.get("cut"),
                color=request.form.get("color"),
                clarity=request.form.get("clarity")
            )
            logging.info(f"Input data collected: {data.__dict__}")

            # Converting input data into a DataFrame
            final_data = data.get_data_as_dataframe()
            logging.info(f"Data converted to DataFrame:\n{final_data}")

            # Initialize the prediction pipeline
            predict_pipeline = PredictionPipeline()
            logging.info("Prediction pipeline initialized.")

            # Get prediction
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)
            logging.info(f"Prediction made: {result}")

            # Render the result page
            return render_template("result.html", final_result=result)
        
        except Exception as e:
            logging.error(f"Error occurred during prediction: {str(e)}")
            return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    logging.info("Starting Flask application.")
    app.run(host="0.0.0.0", port=8080)
