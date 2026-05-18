import os
import sys
import shutil
from datetime import datetime
from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        # NEW ADDITION: Define a timestamped path to back up historical models
        self.timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self.backup_dir = os.path.join("saved_models", self.timestamp)

    def backup_artifacts(self, preprocessor_path, model_path):
        """
        NEW METHOD: Archives trained artifacts to prevent accidental deletion 
        during subsequent training runs.
        """
        try:
            os.makedirs(self.backup_dir, exist_ok=True)
            if os.path.exists(preprocessor_path):
                shutil.copy(preprocessor_path, self.backup_dir)
            if os.path.exists(model_path):
                shutil.copy(model_path, self.backup_dir)
            logging.info(f"Artifacts backed up securely to: {self.backup_dir}")
        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            logging.info("==================================================")
            logging.info("Retraining Pipeline Execution Triggered")
            logging.info("==================================================")

            # Step 1: Trigger Data Ingestion
            logging.info("Step 1: Starting Data Ingestion Phase")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()
            
            # CRITICAL ADDITION: Verify data files actually exist before moving forward
            if not os.path.exists(train_path) or not os.path.exists(test_path):
                raise FileNotFoundError("Ingestion outputs missing or corrupted.")
            logging.info(f"Data Ingestion Success. Train path: {train_path}, Test path: {test_path}")

            # Step 2: Trigger Data Transformation
            logging.info("Step 2: Starting Data Transformation Phase")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_file_path = data_transformation.initiate_data_transformation(
                train_path=train_path, 
                test_path=test_path
            )
            logging.info(f"Data Transformation Success. Preprocessor saved at: {preprocessor_file_path}")

            # Step 3: Trigger Model Training and Evaluation
            logging.info("Step 3: Starting Model Training Phase")
            model_trainer = ModelTrainer()
            r2_score_result = model_trainer.initiate_model_trainer(
                train_array=train_arr, 
                test_array=test_arr
            )
            
            # NEW ADDITION: Backup models immediately upon successful training
            model_file_path = os.path.join("artifacts", "model.pkl")
            self.backup_artifacts(preprocessor_file_path, model_file_path)

            logging.info("==================================================")
            logging.info(f"Retraining Completed Successfully. Champion Model R2 Score: {r2_score_result:.4f}")
            logging.info("==================================================")

            return r2_score_result

        except Exception as e:
            logging.error("Retraining Pipeline failed during execution.")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        pipeline = TrainPipeline()
        final_score = pipeline.run_pipeline()
        print(f"\nExecution Complete! Champion Model R2 Score: {final_score:.4f}")
    except Exception as e:
        print(f"\nPipeline Execution Failed! Details: {e}")
