import pickle
import os
import sys
from src.logger import logging
from src.exception import CustomException


def save_object(obj,obj_path):
    try:
        obj_dir = os.path.dirname(obj_path)
        os.makedirs(obj_dir,exist_ok=True)

        with open(obj_path,"wb") as file_obj:
            pickle.dump(obj,file_obj) 
    except Exception as e:
        raise CustomException(e,sys)