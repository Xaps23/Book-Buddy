from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.config.configuration import AppConfiguration

class TrainingPipeline:

    def __init__(self, app_config: AppConfiguration):
        app_config = AppConfiguration()
        self.data_ingestion = DataIngestion(app_config=app_config)

    def start_training_pipeline(self):
        '''Start the training pipeline by initiating data ingestion.
        :return: None

        '''
        self.data_ingestion.initiate_data_ingestion()
