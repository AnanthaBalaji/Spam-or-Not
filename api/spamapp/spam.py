import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



class SpamIdentify():

    def __init__(self):
        self.sms_data = None
        self.X_train = None
        self.X_train_transformed = None
        self.y_train = None
        self.mnb = MultinomialNB()
        self.vect = None
        self.directory = os.getcwd()
        self.import_file()

    def import_file(self):
        self.sms_data = pd.read_csv(self.directory+'/spamapp/SMSSpamCollection',header=None,names=['Class','sms'],sep="\t")
        self.clean_data()

    def clean_data(self):
        self.sms_data['Class'] = self.sms_data['Class'].map({'spam':0,'ham':1})
        self.split_data()
    
    def split_data(self):
        self.y_train = self.sms_data['Class'].astype(int).values
        self.X_train = self.sms_data['sms'].values
        self.vect = CountVectorizer(stop_words='english')
        self.vect.fit(self.X_train)
        self.X_train_transformed = self.vect.transform(self.X_train)
        self.build_model()

    def build_model(self):
        self.mnb.fit(self.X_train_transformed,self.y_train)
    

    def predict_data(self,txt):
        value=""
        txt_transformed = self.vect.transform([txt])
        y_pred_prob = self.mnb.predict_proba(txt_transformed)
        if y_pred_prob[:1,0]>y_pred_prob[:1,1]:
            value = "Spam"
        else:
            value = "Not Spam"
        return {'prediction':value,
                'spam_prob':(str(100*y_pred_prob[:1,0]).split("["))[1].split("]")[0],
                'ham_prob':(str(100*y_pred_prob[:1,1]).split("["))[1].split("]")[0]}