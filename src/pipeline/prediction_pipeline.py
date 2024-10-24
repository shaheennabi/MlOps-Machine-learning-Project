import os
import sys
import pandas as pd
from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import load_object


class PredictionPipeline:

    def __init__(self):
        logging.info("PredictionPipeline object initialized.")

    def predict(self, features):
        try:
            logging.info("Starting prediction process.")

            # Define paths for preprocessor and model
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            # Load preprocessor and model
            logging.info(f"Loading preprocessor from {preprocessor_path}")
            preprocessor = load_object(preprocessor_path)

            logging.info(f"Loading model from {model_path}")
            model = load_object(model_path)

            # Transform features
            logging.info("Transforming features with preprocessor.")
            scaled_fea = preprocessor.transform(features)
            logging.info(f"Features after transformation: {scaled_fea}")

            # Make predictions
            logging.info("Making predictions with the model.")
            pred = model.predict(scaled_fea)

            logging.info(f"Prediction result: {pred}")

            return pred

        except Exception as e:
            logging.error(f"Error occurred in prediction process: {str(e)}")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

        logging.info(f"CustomData object created with values: {self.__dict__}")

    def get_data_as_dataframe(self):
        try:
            logging.info("Converting custom data to DataFrame.")
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }
            
            # Create DataFrame
            df = pd.DataFrame(custom_data_input_dict)
            logging.info(f"DataFrame created: \n{df}")

            return df
        except Exception as e:
            logging.error(f"Exception occurred while converting data to DataFrame: {str(e)}")
            raise CustomException(e, sys)
