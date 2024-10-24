import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from src.logger.logging import logging
from src.exception.exception import CustomException
from dataclasses import dataclass


@dataclass
class ModelEvaluationConfig:
    pass


class ModelEvaluation:
    def __init__(self):
        pass











    def initiate_model_evaluation(self):
        try:
            pass












        except Exception as e: 
            logging.info()
            raise CustomException(e, sys)

