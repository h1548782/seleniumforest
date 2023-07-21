import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from ipywidgets import Output, VBox, Button

def train_model(X_train, X_test, y_train, y_test):
    # create rf classifier
    global rf
    rf = RandomForestClassifier()
    

    #train the classifier with training data
    rf.fit(X_train, y_train)

    #predict target with test/sim data
    y_pred = rf.predict(X_test)

    #print the accuracy score for the provided test set
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    #print confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)
    print('')
    
    return rf
    

####################################################################

def predict_model(df_sim, index, model):
    global count_ones, prediction_count, prediction_list, y_predicted
    #has to be single line!
    
    received_data = df_sim.loc[index]

    #reshape
    received_data = received_data.values.reshape(1, -1)

    #predict y given the received data input
    y_predicted = rf.predict(received_data)
    print('The Algorithm predicted the following Anomaly State:')
    print(y_predicted)
    
    return y_predicted    