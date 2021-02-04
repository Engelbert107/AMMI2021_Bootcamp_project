def space(start,end,nvals):
    """
    python implemetation of the np.linspace function using generators
    """
    step = (end-start)/nvals
    for i in range(nvals):
        yield start+(i*step)

class RuleBasedModel:   
    """
    Implemenation of a rule based classifier.
    Uses a threshold on three variables: f1, f3, f8. Those were the three variables with the highest correlation values with respect to the class
    """
    def __init__(self):
        """
        Initialize the threshold range to search for values for the optimal threshold
        Initialize the list of features to use
        Initialize an empty threshold list. This list will be filled with the three optimal thresholds after training
        Initialize the acc
        """
        self.threshold_ranges = [[0.1,0.4],[0.1,0.5],[0.1,0.5]]
        self.features = ['f1','f3','f8']
        self.threshold = [0,0,0]
        self.acc = 0
    
    def pred(self,x, threshold = [0,0,0]):
        """
        Function to predict for a single dictionary row
        Uses the provided threshold or the default threshold if not provided
        """    
        if threshold == [0,0,0]:
            threshold = self.threshold 
        if x[self.features[0]] > threshold[0] and x[self.features[1]] > threshold[1] and x[self.features[2]] > threshold[2]:
            return 1
        else:
            return 2

    def train(self, data):
        """
        Train, by searching through the range space in order to find the combination of thresholds that gives the best accuracy
        """
        accuracy = 0
        pair = [0,0]
        space_width = 60
        for x in space(self.threshold_ranges[0][0],self.threshold_ranges[0][1],space_width):
            for y in space(self.threshold_ranges[1][0],self.threshold_ranges[1][1],space_width):
                for z in space(self.threshold_ranges[2][0],self.threshold_ranges[2][1],space_width):
                    temp_pair = [x,y,z]
                    temp_accuracy, a, b = self.accuracy(data,temp_pair)
                    if temp_accuracy > accuracy:
                        accuracy = temp_accuracy
                        pair = temp_pair
        self.threshold = pair
        self.acc = accuracy
        return self.acc

    def test(self, data):
        """
        used to predict on data that does not have class labels
        """
        result = []
        for data_point in data:
            result.append(self.pred(data_point))
        return result

    def predict_with_id(self, id, data):
        """
        Predict for a specific ID
        """
        for x in data:
            if int(id) == int(x["ID"]):
                return self.pred(x)
        else:
            print("ID not found")


    def accuracy(self,data,threshold=[0,0,0]):
        """
        Uses trained threshold to predict on data and get the accuracy
        """
        if threshold == [0,0,0]:
            threshold = self.threshold  
        correct = 0
        total = len(data)
        for data_point in data:
            if data_point["class"] == self.pred(data_point,threshold):
                correct+=1
        return correct/total, correct, total
