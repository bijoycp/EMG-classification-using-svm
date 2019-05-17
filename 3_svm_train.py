
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import numpy as np

from sklearn.externals import joblib

train_data = np.load('train_data.npy',encoding="latin1")

X = np.array([i[0] for i in train_data])
Y = [i[1] for i in train_data]
print(len(X))
print(len(Y))
print((X[0]))
print(Y[0])
print(Y)


clf = svm.SVC(kernel='linear')
clf.fit(X,Y)
filename = 'EMG-model.sav'
joblib.dump(clf, filename)

clf1 = joblib.load(filename)
print("output")
print(clf1.predict([X[0]]))
print(clf1.predict([X[1]]))
print(clf1.predict([X[2]]))
print(clf1.predict([X[3]]))
print(clf.predict([X[4]]))
# print(clf.predict([X[5]]))
