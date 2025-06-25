import os 
import sys
import urllib.request
import zipfile
import shutil
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException


class DataIngestion:
    """
    Handles the ingestion of data: downloading and extracting the dataset.
    """

    def __init__(self, app_config):
        self.data_ingestion_config = app_config.data_ingestion

    def initiate_data_ingestion(self):
        """
        Downloads and extracts the dataset as per configuration.
        """
        try:
            # Get config values
            url = self.data_ingestion_config['dataset_download_url']
            raw_data_dir = self.data_ingestion_config['raw_data_dir']
            ingested_dir = self.data_ingestion_config['ingested_dir']
            dataset_dir = self.data_ingestion_config['dataset_dir']

            # Ensure directories exist
            os.makedirs(raw_data_dir, exist_ok=True)
            os.makedirs(ingested_dir, exist_ok=True)
            os.makedirs(dataset_dir, exist_ok=True)

            # Download dataset
            zip_path = os.path.join(raw_data_dir, "books_data.zip")
            if not os.path.exists(zip_path):
                logging.info(f"Downloading dataset from {url} to {zip_path}")
                urllib.request.urlretrieve(url, zip_path)
                logging.info("Download complete.")
            else:
                logging.info(f"Dataset already exists at {zip_path}, skipping download.")

            # Extract dataset
            logging.info(f"Extracting {zip_path} to {ingested_dir}")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
            logging.info(f"Extraction complete. Dataset available at {ingested_dir}")
            # Copy extracted files to dataset directory
            for filename in os.listdir(ingested_dir):
                src_file = os.path.join(ingested_dir, filename)
                dst_file = os.path.join(dataset_dir, filename)
                if os.path.isfile(src_file):
                    shutil.copy2(src_file, dst_file)
            logging.info(f"Copied extracted files to dataset directory: {dataset_dir}")


            # Optionally remove zip file after extraction
            if os.path.exists(zip_path):
                os.remove(zip_path)
                logging.info(f"Removed zip file {zip_path} after extraction.")

        except Exception as e:
            logging.error("Error during data ingestion.", exc_info=True)
            raise AppException(e, sys) from e
        
   
        