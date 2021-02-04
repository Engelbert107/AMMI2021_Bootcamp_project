from utils import read_data
from model import RuleBasedModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--predict', help='ID of a row in the test file to use for prediction')

args=parser.parse_args()

def main():
    random.seed(0)

    train_file = './train_data.txt'
    test_file = './test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']

    print ("========= Reading train dataset =========")
    # use the read data function you created to read the train data
    train_data = read_data(train_file,train = True, variables = variables)
	
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    test_data = read_data(test_file,train = True, variables = variables) 
	# Read the test  data
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
    # Initialize the classifier you built in model.py and return the necessary values
    random.shuffle(train_data)
    model = RuleBasedModel()
    acc = model.train(train_data)
    print("Train accuracy is:",acc)
	
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
    # use your classifier to do predictions on all the test samples
    #test_result = model.test(test_data) 
	
    print ("========== Done classifying =======.\n")
    # Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    accuracy, numCorrect, total_samples = model.accuracy(test_data)
    print(f"Model's Accuracy {round(accuracy*100)} %, model correctly predicted {numCorrect} out of {total_samples}")
    print('================================================================.\n')

    if args.predict:
        print ("========== Print prediction at ID requested =======")
        print("The predictedlass for the value at index",args.predict,"is: ",model.predict_with_id(int(args.predict),test_data))
        print('================================================================')


    print ("finished.\n")

main()
