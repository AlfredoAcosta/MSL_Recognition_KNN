"""
Choosing the best value for K in KNN through validation set
and implementing this value to classify Statical Mexican Sign Language.
@author: estevez
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Importing dataset (it only contains features of each intances)
# it loads a matrix of size 10500 x 6336. There are 500 images per class,
# 21 clases and each image of size 72 x 88 px i.e 6336 pixels per image.
datos=pd.read_csv('/home/estevez/Documentos/Programas Python/dataTesis/LSM_reduced.csv')

# Generating the vector of labels
target= np.full((500,1),30)
for i in np.arange(21):
    aux = np.full((500,1),i)
    target = np.vstack((target,aux))
target = np.delete(target,slice(0,500),0)

# Train and test set randomly and stratified selected
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(datos, target, test_size=0.2,random_state=0,stratify=target)

# Normalizing data
X_train=X_train/255  
X_test=X_test/255   

# New train and validation set to obtain the best K value
from sklearn.model_selection import train_test_split
new_train, new_test, new_y_train, new_y_test = train_test_split(X_train, y_train, test_size=0.2,random_state=0,stratify=y_train)

# Normalizing data
new_train=new_train/255  
new_test=new_test/255 


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

accuracy_models = []

# Evaluating new train and test set to obtain the best value for K
# this evaluation consist of train and test the KNN algorithm with
# odd values in range [1,39].
for i in range(1,40,2):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(new_train, new_y_train)
    y_pred = knn.predict(new_test)
    acc=accuracy_score(new_y_test,y_pred)
    accuracy_models.append(acc)
    print("Accuracy of classifier with K = {}: ".format(i), acc) 

# Let's plot this accuracy vector
kvalues=np.arange(1,40,2)
plt.plot(kvalues,accuracy_models[:20],'r+')    
plt.xlabel('k values')    
plt.ylabel('accuracy')
plt.title("Accuracy of KNN with validation set")
plt.show() 


# It's easy to see that the best accuracy it's reached with K=1
# but it could turn the model too sensible to any change of 
# features and noise. So K=3 it's a better option.
 
# Now with this value is training the classifier, but with
# the originals train and test set wich cointains all dataset.
# The test set now it's the unseen data.

start = time.time()
knn = KNeighborsClassifier(3) 
knn.fit(X_train, y_train)   
y_pred = knn.predict(X_test)    
acc=accuracy_score(y_test,y_pred)    
print("Accuracy of classifier: ", acc)   
training_time = time.time() - start
print("Time taken to train model: ", training_time)

# Evaluating this 3-NN classifier
labels=["A","B","C","D","E","F","G","H","I","L","M","N","O","P","R","S","T","U","V","W","Y"]
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred, target_names=labels))

y_test=y_test.reshape((2100))
from sklearn.metrics import precision_score
precision_score(y_test, y_pred, average='weighted')

from sklearn.metrics import recall_score
recall_score(y_test, y_pred, average='weighted')

from sklearn.metrics import f1_score
f1_score(y_test, y_pred, average='weighted')


    







