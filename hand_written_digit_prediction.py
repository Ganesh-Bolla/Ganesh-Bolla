# -*- coding: utf-8 -*-
"""Hand Written Digit Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17vMKHcaxhjbXhUCggAHh8wB6rq2U9qQ6

# **Hand Written Digit Prediction**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

df = load_digits()

fig , axes = plt.subplots(nrows = 1 , ncols = 4 , figsize =(10,3))
for ax , image , label in zip(axes , df.images , df.target):
    ax.set_axis_off()
    ax.imshow(image , cmap = plt.cm.gray_r,interpolation = 'nearest')
    ax.set_title("Training : %i" % label)

"""# Data Preprocessing"""

df.images.shape

df.images[0]

df.images[0].shape

n_samples = len(df.images)
data = df.images.reshape((n_samples , -1))

data[0]

data[0].shape

data.shape

"""**Scaling image data**"""

data.min()

data.max()

data = data/16

data.min()

data.max()

data[0]

"""**Splitting the testing and training data**"""

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(data , df.target, test_size = 0.3)

x_test.shape , x_train.shape , y_train.shape , y_test.shape



"""**Random Forest Model**"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(x_train,y_train)

"""**Predict the test data**"""

y_pred = rf.predict(x_test)
print(y_pred)

"""**Model accuracy**"""

from sklearn.metrics import confusion_matrix , classification_report

confusion_matrix(y_test , y_pred)

print(classification_report(y_test , y_pred))