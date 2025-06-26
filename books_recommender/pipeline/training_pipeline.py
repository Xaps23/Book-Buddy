from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.components.stage_01_data_validation import DataValidation
from books_recommender.components.stage_02_data_transformation import DataTransformation
from books_recommender.components.stage_03_model_trainer import ModelTrainer
from books_recommender.config.configuration import AppConfiguration

class TrainingPipeline:

    def __init__(self, app_config: AppConfiguration):
    
        self.data_ingestion = DataIngestion(app_config=app_config)
        self.data_validation = DataValidation(app_config=app_config)
        self.data_transformation = DataTransformation(app_config=app_config)
        self.model_trainer = ModelTrainer(app_config=app_config)


    def start_training_pipeline(self):
        '''Start the training pipeline.
        :return: None

        '''
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_trainer.initiate_model_trainer() 
