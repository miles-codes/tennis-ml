# XGBoost

# Install xgboost following the instructions on this link: http://xgboost.readthedocs.io/en/latest/build.html#

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/csv_files/ready.csv')
X = dataset.iloc[:, 0:7].values
y = dataset.iloc[:, 7].values

# Encoding categorical data
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# labelencoder_X_1 = LabelEncoder()
# X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
# labelencoder_X_2 = LabelEncoder()
# X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
# onehotencoder = OneHotEncoder(categorical_features = [1])
# X = onehotencoder.fit_transform(X).toarray()
# X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fitting XGBoost to the Training set
from xgboost import XGBClassifier

classifier = XGBClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))
print(cm[1][1] / (cm[1][1] + cm[1][0]))
print(cm[0][0] / (cm[0][0] + cm[0][1]))

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score

accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
print()
print(accuracies.mean())
print(accuracies.std())

# from sklearn.model_selection import cross_val_predict
# from sklearn.metrics import confusion_matrix
# y_pred1 = cross_val_predict(classifier, X_train, y_train, cv=10)
# conf_mat = confusion_matrix(y_train, y_pred1)
# print()
# print(conf_mat)
# print(accuracy_score(y_train, y_pred1))
# print(cm[1][1] / (cm[1][1] + cm[1][0]))
# print(cm[0][0] / (cm[0][0] + cm[0][1]))
