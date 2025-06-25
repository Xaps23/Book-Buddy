import os 
import sys
import ast 
import pandas as pd
import pickle
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException

class DataValidation:
    def __init__(self, app_config: AppConfiguration):
        try:
           self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def preprocess_data(self):
        try:
            # Load the books and ratings data
            books_df = pd.read_csv(self.data_validation_config.books_csv_file, sep=";",error_bad_lines=False, encoding='latin-1')
            ratings_df = pd.read_csv(self.data_validation_config.ratings_csv_file, sep=";",error_bad_lines=False, encoding='latin-1')

            # Convert 'book_id' to string type
            books_df['book_id'] = books_df['book_id'].astype(str)
            ratings_df['book_id'] = ratings_df['book_id'].astype(str)

            # Save preprocessed data
            preprocessed_books_path = os.path.join(self.data_validation_config.clean_data_dir, 'preprocessed_books.csv')
            preprocessed_ratings_path = os.path.join(self.data_validation_config.clean_data_dir, 'preprocessed_ratings.csv')
            books_df.to_csv(preprocessed_books_path, index=False)
            ratings_df.to_csv(preprocessed_ratings_path, index=False)

            logging.info(f"Preprocessed books data saved to {preprocessed_books_path}")
            logging.info(f"Preprocessed ratings data saved to {preprocessed_ratings_path}")


    def validate_data(self):
        """
        Validates the ingested data.
        """
        try:
            # Load the books and ratings data
            books_df = pd.read_csv(self.data_validation_config.books_csv_file)
            ratings_df = pd.read_csv(self.data_validation_config.ratings_csv_file)

            # Check for duplicates in books data
            if books_df.duplicated().any():
                logging.warning("Duplicates found in books data.")
                books_df.drop_duplicates(inplace=True)
                logging.info("Duplicates removed from books data.")

            # Check for missing values in books data
            if books_df.isnull().values.any():
                logging.warning("Missing values found in books data.")
                books_df.fillna(method='ffill', inplace=True)
                logging.info("Missing values filled in books data.")

            # Check for duplicates in ratings data
            if ratings_df.duplicated().any():
                logging.warning("Duplicates found in ratings data.")
                ratings_df.drop_duplicates(inplace=True)
                logging.info("Duplicates removed from ratings data.")

            # Check for missing values in ratings data
            if ratings_df.isnull().values.any():
                logging.warning("Missing values found in ratings data.")
                ratings_df.fillna(method='ffill', inplace=True)
                logging.info("Missing values filled in ratings data.")

            # Save cleaned data
            cleaned_books_path = os.path.join(self.data_validation_config.clean_data_dir, 'cleaned_books.csv')
            cleaned_ratings_path = os.path.join(self.data_validation_config.clean_data_dir, 'cleaned_ratings.csv')
            books_df.to_csv(cleaned_books_path, index=False)
            ratings_df.to_csv(cleaned_ratings_path, index=False)

            logging.info(f"Cleaned books data saved to {cleaned_books_path}")
            logging.info(f"Cleaned ratings data saved to {cleaned_ratings_path}")

        except Exception as e:
            raise AppException(e, sys) from e
