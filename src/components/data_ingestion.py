import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

# Get the project root directory dynamically

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join( "artifacts", "train.csv")
    test_data_path: str = os.path.join( "artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            # Read the dataset
            data = pd.read_csv("https://raw.githubusercontent.com/shaheennabi/My_Datasets/refs/heads/main/Gem%20Stone%20Price%20Prediction%20Dataset/dataset.csv")
            logging.info("Reading dataset as DataFrame")

            # Create the artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset saved to artifact folder")
            
            # Perform train-test split
            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")
            
            # Save the train and test datasets
            train_data.to_csv(self.data_ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.data_ingestion_config.test_data_path, index=False)
            logging.info("Data ingestion completed")
            
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error in data ingestion")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
