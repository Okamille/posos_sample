import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from joblib import dump

input_train = pd.read_csv('../data/input_train.csv')
X = input_train['question'].values

output_train = pd.read_csv('../data/output_train.csv')
y = output_train['intention'].values

X_train, X_test, y_train, y_test = train_test_split(X, y)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# TODO : change default parameters of SVC
clf = SVC()
clf.fit(X_train, y_train)

filename = 'SVC.joblib'

dump(clf, filename)