import os
import sys
from src.logger import logging
from src.exception import CustomException

from flask import Flask,request,render_template,jsonify
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Home page initiated.")
    return render_template("home.html")
@app.route('/predict',methods=["POST"])
def predict():
    logging.info("prediction is called.")
    data = CustomData(
        age = request.form.get('age'),
        gender = request.form.get('gender'),
        relationship = request.form.get('relationship'),
        Occupation_Status = request.form.get('Occupation_Status'),
        use_social_media = request.form.get('use_social_media'),
        average_time_spent = request.form.get('average_time_spent'),
        using_social_media_without_purpose = request.form.get('using_social_media_without_purpose'),
        distracted_by_social_media = request.form.get('distracted_by_social_media'),
        feel_restless = request.form.get('feel_restless'),
        easily_distracted = request.form.get('easily_distracted'),
        bothered_by_worries = request.form.get('bothered_by_worries'),
        difficult_to_concentrate = request.form.get('difficult_to_concentrate'),
        compare_yourself = request.form.get('compare_yourself'),
        seek_validation = request.form.get('seek_validation'),
        feel_depressed = request.form.get('feel_depressed'),
        interest_fluctuate = request.form.get('interest_fluctuate'),
        sleep_issue = request.form.get('sleep_issue'),
        instagram = request.form.get('instagram'),
        snapchat = request.form.get('snapchat'),
        facebook = request.form.get('facebook'),
        twitter = request.form.get('twitter'),
        youtube = request.form.get('youtube'),
        reddit = request.form.get('reddit'),
        whatsapp = request.form.get('whatsapp'),
        linkedin = request.form.get('linkedin')
    )
    df = data.get_data_as_data_frame()
    logging.info(f"Before prediction:{df}")
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(df)
    logging.info(f"prediction:{prediction}")
    return jsonify({'prediction': prediction})


if __name__=="__main__":
    app.run(host='0.0.0.0')