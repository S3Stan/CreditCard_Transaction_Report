# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import dask.dataframe as dd

# datafile URL

#df = dd.read_csv('your_dataset.csv')
creditcardData_p1 = pd.read_csv("Analysis_repo/Datasets/creditCardData_p1of2.csv" , sep=",")
creditcardData_p2 = pd.read_csv("Analysis_repo/Datasets/creditCardData_p2of2.csv" , sep=",")
creditcardData_prediction = pd.read_csv("Analysis_repo/Datasets/creditCardData_prediction.csv", sep=",")


# exception to catch what happens when dataset is called 
class datasetNotFoundException(Exception):
    pass 

# imports 
def sendCreditCardData_part1():
    analysis_size_data = creditcardData_p1
    return analysis_size_data

def sendCreditCardData_part2():
    analysis_size_data = creditcardData_p2
    return analysis_size_data


def sendPredictionDataset():
    return creditcardData_prediction


import dask.dataframe as dd


# Datset saving code
# # Save the DataFrame to a CSV file
#df.to_csv('dataset.csv', index=False)


# creditcardData = pd.read_csv("C:/Users/stanf/OneDrive/Desktop/creditcard_mod.csv" , sep=",")
# df = creditcardData.iloc[45000:90000]
# print(df)


# df.to_csv('Analysis_repo/Datasets/creditCardData_p2of2.csv', index=False)