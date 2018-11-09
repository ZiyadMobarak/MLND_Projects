#import the required folders
import numpy as np
import pandas as pd
from IPython.display import display

#import visualization required package
import visuals as vs

#pretty display of the inline data
%matplotlib inline

#Load the dataset
file_name = "titanic_data.csv"
imported_data = pd.read_csv(file_name)

#print the first few records
display(imported_data.head())

#Take only the outcomes:
the_outcomes_column = imported_data['Survived']
imported_data = imported_data.drop('Survived', axis = 1)

#Show the new dataset after removing the outcomes:
display(imported_data.head())

#Define the required function to calculate the accuracy:
def calc_accuracy(outcomes, predictions):
    "This function calculate the accuracy of the given predictions to the outcomes"

    #Ensure that both lists have same number of elements
    if len(outcomes) == len(predictions):
        #Compute the the accuracy and return it
        return "The accuracy is {:2f}%".format((outcomes == predictions).mean() * 100)

    #If they have different numbers
    else:
        return "The two lists have different number of elements"

#Test the accuracy of the predictions of the first five only assuming you predicit that all of them suvived
all_five_suvived = pd.Series(np.ones(5, dtype = int))
print(calc_accuracy(the_outcomes_column, all_five_suvived))

#define a function the always predict negative (return list of negatives)
def all_not_survived(outcomes):
    "This function will return corresponding negative zero for any value in the outcome"

    predictions = [] #Prepare a new empty list
    for passenger in outcomes.iterrows():
        predictions.append(0) ;

    #Return the predicitions in Pandas Series for easy manipulation
    return pd.Series(predicitons)

#Make the list of all negartive predeictions by calling the function above
all_not_survived(the_outcomes_column)

#Find the accuracy of predicting all didn't Survived
print(calc_accuracy(the_outcomes_column, all_not_survived(the_outcomes_column)))
