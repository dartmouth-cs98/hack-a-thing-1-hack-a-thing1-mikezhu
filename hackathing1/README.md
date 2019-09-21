# hack-a-thing-1-mikezhu

## Sept 21, 2019

## Description

For my hackathing, I followed a sentiment analysis tutorial for Python/scikit-learn and implemented the script into a website built on Meteor, a platform for creating web apps in JS. I wanted to work with something that involved machine learning, which I am interested in, and sentiment analysis seemed like a good choice. Also, I had never created a website before (I haven't taken CS52) so I wanted to learn the basics for that using an up and rising platform.

The website is super simple, as I just wanted to learn the basics for creating a website, so it essentially just takes a phrase and uses the back-end mdoels to predict the sentiment of that phrase.

The tutorials for creating the sentiment analyzer and a basic React website built on Meteor are found at
- https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/
- https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn
- https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
- https://www.meteor.com/tutorials/react/creating-an-app
- https://reactjs.org/docs/forms.html

## Work

I worked by myself on this assignment!

## What did and didn't work

The sentiment analysis tutorial was very thorough, so I essentially used the code they provided to create the sentiment analysis tool. This was also great review for the material I learned in CS74 (Machine Learning), which I took last year.

The sentiment analysis tutorial also chose to use the RandomForestClassifier; I wanted to try different machine learning algorithms to see if there were any that provided a better accuracy, so I also tried the K-nearest neighbors (KNN) algorithm and the support vector machine (SVM) models. Both tutorials were provided above. The SVM model provided the highest accuracy on the same test set, so I decided to utilize the SVM classifier in my sentiment analysis tool.

It was initially challenging to download all the dependencies for Meteor and then Meteor itself, but once I had finished installing everything, the Meteor/React tutorial was super helpful and very easy to use.