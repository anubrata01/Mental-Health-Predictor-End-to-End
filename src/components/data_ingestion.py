import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

# Train test split 
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_path :str= os.path.join("artifacts","raw.csv")
    train_path :str= os.path.join("artifacts","train.csv")
    test_path :str= os.path.join("artifacts","test.csv")
class DataIngestion:
    def __init__(self):
        self.data_config = DataIngestionConfig()
    def initiate_data_ingesion(self):
        logging.info("Data Ingesion initiated")
        try:
            df = pd.read_csv("D:\Mental Health Predictor\mental health data\social midia and mental health\mental_health_data_processed.csv")
            logging.info("Import data sucessful.")
            logging.info("Train test split intitiated")
            train_data,test_data = train_test_split(df,test_size=0.1,random_state=42)
            os.makedirs(os.path.dirname(self.data_config.raw_path), exist_ok=True)
            df.to_csv(self.data_config.raw_path,index=False,header=True)
            train_data.to_csv(self.data_config.train_path,index=False,header=True)
            test_data.to_csv(self.data_config.test_path,index=False,header=True)

            logging.info("Data Ingesion completed")

            return(
                self.data_config.train_path,
                self.data_config.test_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingesion()