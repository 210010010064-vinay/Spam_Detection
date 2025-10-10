import sys
from src.cloud_storage.local_storage import LocalStorageService 
from src.entity.artifact_entity import ModelPusherArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelPusherConfig
from src.exception import SpamhamException
from src.logger import logging

class ModelPusher:
    def __init__(self,model_trainer_artifact: ModelTrainerArtifact,model_pusher_config: ModelPusherConfig,):
        self.local_storage = LocalStorageService()
        self.model_trainer_artifact = model_trainer_artifact
        self.model_pusher_config = model_pusher_config

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        logging.info("Entered initiate_model_pusher method of ModelPusher class")

        try:
            # Save the model locally (copy from trained_model_file_path to model_pusher_config.local_model_path)
            from shutil import copyfile

            logging.info("Saving model to local project directory")
            copyfile(self.model_trainer_artifact.trained_model_file_path,self.model_pusher_config.local_model_path)

            model_pusher_artifact = ModelPusherArtifact(local_model_path=self.model_pusher_config.local_model_path ) 

            logging.info("Saved model to local directory")
            logging.info(f"Model pusher artifact: [{model_pusher_artifact}]")
            logging.info("Exited initiate_model_pusher method of ModelPusher class")

            return model_pusher_artifact

        except Exception as e:
            raise SpamhamException(e, sys) from e
