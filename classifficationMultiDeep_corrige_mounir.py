# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:04:16 2021
https://www.datacamp.com/community/tutorials/deep-learning-python
https://github.com/benprano/Hybrid-Deep-Learning-model/blob/master/hybrid_model.py
@author: MAROUANE
"""

from keras.models import Sequential
from keras.layers import Dense

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils


df1 = pd.read_csv('DelayedMessage.csv',sep=";")
df2=pd.read_csv('DataReplay.csv',sep=";")
df=pd.concat([df2, df1])

## Split features and labels
X = df.drop("TypeAttack", axis=1)
y = df["TypeAttack"]

# Hela il manquait la transformation des valeurs des classes en une suite d'entiers (on ne peut pas laisser 0, 11 et 12 il faut la remplacer par une suite 0, 1 et 2)
y[y==11] = 1
y[y==12] = 2
# Standardize the dataset
StandardScaler = preprocessing.StandardScaler()
X = StandardScaler.fit_transform(X)

# encode class values as integers

encoder = LabelEncoder()

encoder.fit(y)

encoded_Y = encoder.transform(y)

# convert integers to dummy variables (i.e. one hot encoded)

dummy_y = np_utils.to_categorical(encoded_Y)

X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size = 0.2, random_state = 42)

 ## Deep Learning model DNN
model = Sequential()
first_layer=64
hidden_activation="relu"
second_layer=32
third_layer=16
output_activation="softmax"
model.add(Dense(first_layer, input_shape=(X.shape[1],), activation=hidden_activation))
#couche intemediaire
model.add(Dense(second_layer, activation=hidden_activation))
model.add(Dense(third_layer, activation=hidden_activation))
#derniere couche
model.add(Dense(3, activation=output_activation))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=64)

# evaluate the keras model
_, accuracy = model.evaluate(X_test, y_test)

print('Accuracy: %.2f' % (accuracy*100))

pred= model.predict(X_test)
#decodage des predictions
pred = np.argmax(pred, axis=1)

#decodage du y_test
y_test_decodage = np.argmax(y_test, axis=1)


print(classification_report(y_test_decodage, pred))
