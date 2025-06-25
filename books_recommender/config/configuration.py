import os
import sys
import yaml
from books_recommender.logger.log import logging
from books_recommender.utils.util import read_yaml_file
from books_recommender.exception.exception_handler import AppException
from books_recommender.entity.config_entity import DataIngestionConfig 
from books_recommender.constant import *

class AppConfiguration:
    def __init__(self, config_file_path ="config/config.yaml"):
        try: 
            with open(config_file_path, 'r') as f:
              config = yaml.safe_load(f)
            self.data_ingestion = config["artifacts_config"]["data_ingestion_config"]
        except Exception as e:
            raise AppException(e, sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.data_ingestion
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

           
            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])
            
            response = DataIngestionConfig(
                dataset_dowmload_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )
            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e


