from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys
import os
import warnings
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    logging.info("the execution has started")  # Use lowercase "info" instead of "INFO"

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")  # Use lowercase "info" instead of "INFO"
        raise CustomException(e, sys)
