from utils import read_data
#from model import RuleBasedModel


def main():

    train_file = './train_data.txt'
    test_file = './test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']


    print ("========= Reading train dataset =========")
    train_data = read_data(train_file,train = True, variables = variables)
    print(train_data[0])
	# use the read data function you created to read the train data
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    test_data = read_data(test_file,train = False, variables = variables) 
    print(test_data[0])
	# Read the test  data
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
	# Initialize the classifier you built in model.py and return the necessary values
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
	# use your classifier to do predictions on all the test samples
    print ("========== Done classifying =======")

    	# TO-DO
	# Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    print(f"Model's Accuracy {round(accuracy)} %, model correctly predicted {numCorrect} out of {total_samples}")
    print('================================================================')


    print ("finished.\n")

main()
