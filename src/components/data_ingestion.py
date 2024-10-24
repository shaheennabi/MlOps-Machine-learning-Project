import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path



@dataclass
class DataIngestionConfig:
    pass


class DataIngestion:
    def __init__(self):
        pass











    def initiate_data_ingestion(self):
        try:
            pass












        except Exception as e: 
            logging.info()
            raise CustomException(e, sys)

