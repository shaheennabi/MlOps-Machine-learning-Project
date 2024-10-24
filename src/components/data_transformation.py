import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from  sklearn.preprocessing import OrdinalEncoder, StandardScaler
from src.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    pass


class DataTransformation:
    def __init__(self):
        pass











    def initiate_data_trasformation(self):
        try:
            pass












        except Exception as e: 
            logging.info()
            raise CustomException(e, sys)

