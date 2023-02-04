
from sensor.utils import get_collection_as_dataframe
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
from sensor.components import data_ingestion
import os,sys

if __name__ == '__main__':
    try:
        training_pipeline_config=config_entity.TrainingPipelineConfig()
        data_ingestion_config=config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion=data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())
    except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)