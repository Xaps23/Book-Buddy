from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.components.stage_01_data_validation import DataValidation
from books_recommender.config.configuration import AppConfiguration

class TrainingPipeline:

    def __init__(self, app_config: AppConfiguration):
    
        self.data_ingestion = DataIngestion(app_config=app_config)
        self.data_validation = DataValidation(app_config=app_config)

    def start_training_pipeline(self):
        '''Start the training pipeline by initiating data ingestion.
        :return: None

        '''
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
