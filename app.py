from flask import Flask, render_template, jsonify


from src.pipeline.prediction_pipeline import PredictionPipeline,  CustomData


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)