# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7JDefhQZBRoukeo3NFLE7nlwdx2EFU_
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import math
import seaborn as sns
from tensorflow import keras
from tensorflow.keras import layers

training_data_original

number_of_container_conveyor = training_data_original.pop('number_of_container_conveyor')
for i in range(5):
    training_data_original['number_of_container_conveyor '+str(i+1)] = (number_of_container_conveyor == 1)*1.0
training_data_original

training_data = training_data_original[['Pick_Time', 'volume_of_items', 'Total_Weight_of_items_present_in_container', 'volume_of_items_present_in_container']]
training_data = pd.concat([training_data, training_data_original[training_data_original.columns[21:]]], axis = 1)
training_data

msk = np.random.rand(len(training_data)) < 0.8
train = training_data[msk]
test = training_data[~msk]

train

sns.pairplot(train[["volume_of_items", "Total_Weight_of_items_present_in_container", "volume_of_items_present_in_container"]], diag_kind="kde")
plt.show()

train_stats = train.describe()
train_stats = train_stats.transpose()
train_stats

test_stats = test.describe()
test_stats = test_stats.transpose()
test_stats

train_labels = train.pop('Pick_Time')
test_labels = test.pop('Pick_Time')

def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train = norm(train)
normed_test = norm(test)

def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train.keys())]),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mean_squared_error',
                optimizer=optimizer,
                metrics=['mean_absolute_error', 'mean_squared_error'])
  return model

model = build_model()

model.summary()

