from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.config.configuration import AppConfiguration

if __name__ == "__main__":
    app_config = AppConfiguration()
    obj = TrainingPipeline(app_config)
    obj.start_training_pipeline()