from src.ml.model.local_estimator import SpamhamDetector
from src.logger import logging
from src.entity.config_entity import DataTransformationConfig , ModelTrainerConfig
from src.constant.training_pipeline import *
from src.entity.config_entity import training_pipeline_config
from src.entity.config_entity import Prediction_config, PredictionPipelineConfig

from src.entity.config_entity import DataTransformationConfig , ModelTrainerConfig
from src.logger import logging
from src.utils.main_utils import MainUtils

from src.exception import SpamhamException
import pandas as pd
import numpy as np
import sys

import logging
import sys
from pandas import DataFrame
import pandas as pd



        
        
    


class PredictionPipeline:
    def __init__(self):
        self.utils = MainUtils()
        
        
    def get_trained_model(self):
        try:
            prediction_config = PredictionPipelineConfig()
            model = SpamhamDetector(local_model_path=prediction_config.model_file_name) 
            return model
        except Exception as e:
            raise SpamhamException(e, sys) from e
        

    def run_pipeline(self, input_data: list):
        try:
            model = self.get_trained_model()
            text_col = "Message"

            if isinstance(input_data, list) and len(input_data) > 0:
                if isinstance(input_data[0], dict):
                    input_df = pd.DataFrame(input_data)
                else:
                    input_df = pd.DataFrame(input_data, columns=[text_col])
            else:
                raise SpamhamException("Input data is empty or not in expected format", sys)

            if text_col not in input_df.columns:
                raise SpamhamException(f"Expected text column '{text_col}' not found in input", sys)

            # Convert text column to string
            input_df[text_col] = input_df[text_col].astype(str)

            # Pass only the text column to the model (as a DataFrame)
            prediction = model.predict(input_df[[text_col]])

            return prediction

        except Exception as e:
            raise SpamhamException(e, sys) from e
            
            
        

 
        

        