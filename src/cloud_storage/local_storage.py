import pickle
import logging
import sys

class LocalStorageService:

    def load_model(self, model_path: str) -> object:
        try:
            logging.info(f"Loading model from {model_path}")
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            logging.info(f"Model loaded successfully from {model_path}")
            return model
        except FileNotFoundError as e:
            logging.error(f"File not found: {model_path} - {e}")
            raise
        except pickle.UnpicklingError as e:
            logging.error(f"Error unpickling file: {model_path} - {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while loading model from {model_path} - {e}")
            raise

    def save_model(self, model, model_path: str) -> None:
        try:
            logging.info(f"Saving model to {model_path}")
            with open(model_path, "wb") as f:
                pickle.dump(model, f)
            logging.info(f"Model saved successfully to {model_path}")
        except Exception as e:
            logging.error(f"Error saving model to {model_path} - {e}")
            raise
