# Michael Zhu COSC 98 Milestone 1
# I was interested in sentiment analysis and decided to play around with it using Scikit-learn.
# I followed/used a tutorial given below:
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

import numpy as np 
import pandas as pd 
import re
import nltk 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"

def main():
	classifier = import_data(source_url)
	#sentence = process_sentence(u_input)
	#predictions = classifier.predict(sentence)

def import_data(url):
	print("Importing data...")
	dataset = pd.read_csv(url)	# acquire data from url
	
	# split up dataset into feature and labels
	feature_set = dataset.iloc[:, 10].values 	# feature set: the tweet content (11th column)
	label_set = dataset.iloc[:, 1].values		# label set: the sentiment (2nd column)

	# data pre-processing
	# removes special characters, excess spaces, etc. Also converts to lowercase.
	# this is directly copy-and-pasted from the tutorial
	processed_features = []

	for sentence in range(0, len(feature_set)):
	    # Remove all the special characters
	    processed_feature = re.sub(r'\W', ' ', str(feature_set[sentence]))

	    # remove all single characters
	    processed_feature= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

	    # Remove single characters from the start
	    processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature) 

	    # Substituting multiple spaces with single space
	    processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

	    # Removing prefixed 'b'
	    processed_feature = re.sub(r'^b\s+', '', processed_feature)

	    # Converting to Lowercase
	    processed_feature = processed_feature.lower()

	    processed_features.append(processed_feature)

	# convert the pre-processed tweets into TF-IDF vectors
	vectorizer = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words('english'))
	processed_features = vectorizer.fit_transform(processed_features).toarray()

	# divide the data into training and test sets
	X_train, X_test, y_train, y_test = train_test_split(processed_features, label_set, test_size=0.2, random_state=0)
	
	# # Using the Random Forest classifier, make the model and predictions
	# rf_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
	# rf_classifier.fit(X_train, y_train)
	# rf_predictions = rf_classifier.predict(X_test)
	# print(accuracy_score(y_test, rf_predictions))

	# # Using KNN...
	# knn_classifier = KNeighborsClassifier(n_neighbors=5)
	# knn_classifier.fit(X_train, y_train)
	# knn_predictions = knn_classifier.predict(X_test)
	# print(accuracy_score(y_test, knn_predictions))

	# Using SVM...
	svm_classifier = SVC(kernel='linear')
	svm_classifier.fit(X_train, y_train)
	svm_predictions = svm_classifier.predict(X_test)
	# print(accuracy_score(y_test, svm_predictions))
	return svm_classifier

def process_sentence(u_input):
	pass

main()




