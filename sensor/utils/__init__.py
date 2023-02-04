import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from the database {database_name} and {collection_name}")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Total Columns are : {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping _id column from dataframe")
            df.drop("_id",axis=1)
        logging.info(f"Shape are {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)





