import os 
import sys
import pandas as pd
import pickle
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException

class DataTransformation:
    def __init__(self, app_config: AppConfiguration):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_transformer(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)
            book_pivot = df.pivot_table(columns='user_id', index='title', values= 'rating')
            logging.info(f" Shape of books pivot data: {books_pivot.shape}")
            book_pivot.fillna(0, inplace=True)

            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(book_pivot,open(os.path.join(self.data_transformation_config.transformed_data_dir," ")))
            logging.info(f"Saved pivot table data to {self.data_transformation_config.transfromed_data_dir," "}")


            books.rename(columns={'Book-Title': 'title',
                                 'Book-Author': 'author',
                                 "Year-Of-Publication": 'year',
                                 "Publisher": 'publisher',
                                 "Image-URL-S": 'image_url',}, inplace=True)
            

            ratings.rename(columns={"User-ID": 'user_id',
                                    'Book-Rating': 'rating'}, inplace=True)
            
            x = ratings['user_id'].value_counts() > 200
            y = x[x].index
            ratings = ratings[ratings['user_id'].isin(y)]

            ratings_with_books = ratings.merge(books, on='ISBN')
            number_rating = ratings_with_books.groupby('title')['rating'].count().reset_index()
            number_rating.rename(columns={'rating': 'number_of_ratings'}, inplace=True)
            final_rating = ratings_with_books.merge(number_rating, on='title')

            final_rating =final_rating[final_rating['number_of_ratings'] > 50]

            final_rating.drop_duplicates(['user_id', 'title'], inplace=True)
            logging.info(f" Shape of final_rating data: {final_rating.shape}")
            
            #Saving the cleaned data for transformation
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir, 'clean_data.csv'), index=False)
            logging.info(f"Saved cleaned data to {self.data_validation_config.clean_data_dir}")

            #saving final_rating objects fro web app
            os.makedirs(self.data_validation_config.serialized_object_dir, exist_ok=True)
            pickle.dump(final_rating,open(os.path.join(self.data_validation_config.serialized_object_dir, 'final_rating.pkl'),'wb'))
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_object_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_validation(self):
            try:
                logging.info(f"{'='*20} Data Validation log started.{'='*20} ")
                self.preprocess_data()
                logging.info(f"{'='*20} Data Validation log completed.{'='*20} \n\n")
            except Exception as e:
                raise AppException(e, sys) from e
        