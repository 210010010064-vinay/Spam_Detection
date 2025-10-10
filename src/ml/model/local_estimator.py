from src.cloud_storage.local_storage import LocalStorageService
from src.exception import SpamhamException
from src.ml.model.estimator import SpamhamDetectionModel
import sys
from pandas import DataFrame
import os


class SpamhamDetector:
    
    def __init__(self, local_model_path: str):
        
        self.local_model_path : str = local_model_path
        self.local_storage = LocalStorageService()
        self.loaded_model: SpamhamDetectionModel = None

    def is_model_present(self) -> bool:
        try:
            return os.path.exists(self.local_model_path)
        except Exception as e:
            print(e)
            return False

    def load_model(self) -> SpamhamDetectionModel:
      
        try:
            return self.local_storage.load_model(self.local_model_path)
        except Exception as e:
            raise SpamhamException(e, sys) from e

    def save_model(self, model,remove: bool = False) -> None:
        
        try:
            self.local_storage.save_model(model, self.local_model_path)
        except Exception as e:
            raise SpamhamException(e, sys) from e

    def predict(self, dataframe: DataFrame):
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe)
        except Exception as e:
            raise SpamhamException(e, sys) from e
