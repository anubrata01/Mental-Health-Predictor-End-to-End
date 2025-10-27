import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import pandas as pd
import pickle

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            logging.info("predict initiated.")
            preprocessor_path = os.path.join("artifacts","transform.pkl")
            model_path = os.path.join("artifacts","model.pkl")
            logging.info('loading preprocessor and model.')
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            logging.info("scaling features using preprocessor.")
            scaled_data = preprocessor.transform(features)
            logging.info("Assign to a clusters.")
            preds = model.predict(scaled_data)
            logging.info(f"prediction:{preds}")
            cluster_names = {
                0: 'Mature Light Users',
                1: 'Highly Addicted Youth',
                2: 'Moderate Student Users'
            }

            return cluster_names[preds[0]]
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
             age: int,
             gender: int,
             relationship: int,
             Occupation_Status: int,
             use_social_media: int,
             average_time_spent: str,
             using_social_media_without_purpose: int,
             distracted_by_social_media: int,
             feel_restless: int,
             easily_distracted: int,
             bothered_by_worries: int,
             difficult_to_concentrate: int,
             compare_yourself: int,
             seek_validation: int,
             feel_depressed: int,
             interest_fluctuate: int,
             sleep_issue: int,
             instagram: int,
             snapchat: int,
             facebook: int,
             twitter: int,
             youtube: int,
             reddit: int,
             whatsapp: int,
             linkedin: int):    
        self.age = age
        self.gender = gender
        self.relationship = relationship
        self.Occupation_Status = Occupation_Status
        self.use_social_media = use_social_media
        self.average_time_spent = average_time_spent
        self.using_social_media_without_purpose = using_social_media_without_purpose
        self.distracted_by_social_media = distracted_by_social_media
        self.feel_restless = feel_restless
        self.easily_distracted = easily_distracted
        self.bothered_by_worries = bothered_by_worries
        self.difficult_to_concentrate = difficult_to_concentrate
        self.compare_yourself = compare_yourself
        self.seek_validation = seek_validation
        self.feel_depressed = feel_depressed
        self.interest_fluctuate = interest_fluctuate
        self.sleep_issue = sleep_issue
        self.instagram = instagram
        self.snapchat = snapchat
        self.facebook = facebook
        self.twitter = twitter
        self.youtube = youtube
        self.reddit = reddit
        self.whatsapp = whatsapp
        self.linkedin = linkedin

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "gender": [self.gender],
                "relationship": [self.relationship],
                "Occupation Status": [self.Occupation_Status],
                "use social media": [self.use_social_media],
                "average time spend on social media": [self.average_time_spent],
                "using Social media without a specific purpose": [self.using_social_media_without_purpose],
                "distracted by Social media while working": [self.distracted_by_social_media],
                "feel restless if haven't used Social media in a while": [self.feel_restless],
                "how easily distracted are you": [self.easily_distracted],
                "how much are you bothered by worries": [self.bothered_by_worries],
                "find it difficult to concentrate on things": [self.difficult_to_concentrate],
                "how often do you compare yourself": [self.compare_yourself],
                "seek validation from features of social media": [self.seek_validation],
                "feel depressed or down": [self.feel_depressed],
                "how frequently interest fluctuate daily": [self.interest_fluctuate],
                "sleep issue": [self.sleep_issue],
                "facebook": [self.facebook],
                "instagram": [self.instagram],
                "youtube": [self.youtube],
                "snapchat": [self.snapchat],
                "reddit": [self.reddit]
            }


            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


        
