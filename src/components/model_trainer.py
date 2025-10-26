import os
import sys
import numpy as np

from src.logger import logging
from src.exception import CustomException

from src.utils import save_object
from sklearn.cluster import KMeans

from dataclasses import dataclass

@dataclass
class ModelTrainConfig:
    model_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainConfig()
        logging.info("Model trainer initiated.")
    def model_train(self,scaled_data):
        try:
            logging.info("Model initiated.")
            k_means = KMeans(n_clusters=3, random_state=42)
            k_means.fit(scaled_data)
            save_object(k_means,self.config.model_path)
            logging.info("Model saved.")

            unique_label = np.unique(k_means.labels_)
            logging.info(f"Unique Lables are: {unique_label}")
            return unique_label
        except Exception as e:
            raise CustomException(e,sys)
