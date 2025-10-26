import os
import sys
from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.utils import save_object


# Data transformation config
@dataclass
class DataTransformConfig:
    preprocessor_path = os.path.join("artifacts","transform.pkl")
class InitiateDataTransformation:
    def __init__(self):
        self.transform_path = DataTransformConfig()
        logging.info("Data Trnasform Config intiated.")
    def data_transformation_obj(self,columns): # columns requires df.columns
        try:
            cat_data=[
                'gender',
                'relationship',
                'Occupation Status',
                'use social media',
                'average time spend on social media'
            ]
            num_data= [x for x in columns if x not in cat_data]

            logging.info("Categical and numerical data is separated.")
            logging.info("pipeline is initiated")
            cat_pipe=Pipeline(steps=[
                ("Label encoding",OrdinalEncoder()),
                ("Scaled the labels datset",StandardScaler())
            ])
            num_pipe=Pipeline(steps=[
                ("Scaling the num dataset",StandardScaler())
            ])
            logging.info("pipeline setup done.")
            logging.info(f"cat column:{cat_data}")
            logging.info(f"num data:{num_data}")
            logging.info("columnn transformer initiated.")
            preprocessor= ColumnTransformer(
                [
                    ("categorical transformation",cat_pipe,cat_data),
                    ("numerical tranformation",num_pipe,num_data)
                ]
            )
            logging.info("preprocessor setup done.")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        

    # Initiating data transformation
    def data_transform_initiate(self,train_data_path,test_data_path):
        logging.info("Data tranformation intiated.")
        try:
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            pre_processing_obj = self.data_transformation_obj(train_data.columns)
            train_array=pre_processing_obj.fit_transform(train_data)
            test_array = pre_processing_obj.transform(test_data)

            logging.info("saving preprocrssing object.")
            save_object(pre_processing_obj,self.transform_path.preprocessor_path)
            return(train_array,test_array)
        except Exception as e:
            raise CustomException(e,sys)
        
