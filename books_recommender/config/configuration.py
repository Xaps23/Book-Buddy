import os
import sys
import yaml
from books_recommender.logger.log import logging
from books_recommender.utils.util import read_yaml_file
from books_recommender.exception.exception_handler import AppException
from books_recommender.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from books_recommender.constant import *

class AppConfiguration:
    def __init__(self, config_file_path="config/config.yaml"):
        try:
            with open(config_file_path, 'r') as f:
                config = yaml.safe_load(f)
            self.data_ingestion = config["artifacts_config"]["data_ingestion_config"]
            self.data_validation = config["artifacts_config"]["data_validation_config"]
            self.data_transformation = config["artifacts_config"].get("data_transformation_config", {})
            self.artifacts_dir = config["artifacts_config"]["artifacts_dir"]
            self.configs_info = config
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.data_ingestion
            response = DataIngestionConfig(
                dataset_dowmload_url=data_ingestion_config['dataset_download_url'],
                raw_data_dir=data_ingestion_config['raw_data_dir'],
                ingested_dir=data_ingestion_config['ingested_data_dir']
            )
            logging.info(f"Data Ingestion Config: {response}")
            return response
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.data_validation
            clean_data_dir = data_validation_config['clean_data_dir']
            serialized_object_dir = data_validation_config['serialized_object_dir']
            books_csv_file = data_validation_config['books_csv_file']
            ratings_csv_file = data_validation_config['ratings_csv_file']

            response = DataValidationConfig(
                clean_data_dir=clean_data_dir,
                serialized_object_dir=serialized_object_dir,
                books_csv_file=books_csv_file,
                ratings_csv_file=ratings_csv_file
            )
            logging.info(f"Data Validation Config: {response}")
            return response
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            data_transformation_config = self.data_transformation
            data_validation_config = self.data_validation

            clean_data_file_path = os.path.join(
                data_validation_config['clean_data_dir'], 'clean_data.csv'
            )
            transformed_data_file_path = os.path.join(
                data_transformation_config['transformed_data_dir'], 'transformed_data.csv'
            )

            response = DataTransformationConfig(
                clean_data_dir=clean_data_file_path,
                transformed_dir=transformed_data_file_path
            )
            logging.info(f"Data Transformation Config: {response}")
            return response
        except Exception as e:
            raise AppException(e, sys) from e


