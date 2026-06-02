import numpy as np
import math
from collections import Counter
import time


class DecisionNode:
    """Class to represent a nodes or leaves in a decision tree."""

    def __init__(self, left, right, decision_function, class_label=None):
        """
        Create a decision node with eval function to select between left and right node
        NOTE In this representation 'True' values for a decision take us to the left.
        This is arbitrary, but testing relies on this implementation.
        Args:
            left (DecisionNode): left child node
            right (DecisionNode): right child node
            decision_function (func): evaluation function to decide left or right
            class_label (value): label for leaf node
        """
        self.left = left
        self.right = right
        self.decision_function = decision_function
        self.class_label = class_label

    def decide(self, feature):
        """Determine recursively the class of an input array by testing a value
           against a feature's attributes values based on the decision function.

        Args:
            feature: (numpy array(value)): input vector for sample.

        Returns:
            Class label if a leaf node, otherwise a child node.
        """

        if self.class_label is not None:
            return self.class_label

        elif self.decision_function(feature):
            return self.left.decide(feature)

        else:
            return self.right.decide(feature)


def load_csv(data_file_path, class_index=-1):
    """Load csv data in a numpy array.
    Args:
        data_file_path (str): path to data file.
        class_index (int): slice index for data labels.
    Returns:
        features, classes as numpy arrays if class_index is specified,
            otherwise all as nump array.
    """

    handle = open(data_file_path, 'r')
    contents = handle.read()
    handle.close()
    rows = contents.split('\n')
    out = np.array([[float(i) for i in r.split(',')] for r in rows if r])

    if(class_index == -1):
        classes= out[:,class_index]
        features = out[:,:class_index]
        return features, classes
    elif(class_index == 0):
        classes= out[:, class_index]
        features = out[:, 1:]
        return features, classes

    else:
        return out


def build_decision_tree():
    """Create a decision tree capable of handling the sample data contained in the ReadMe.
    It must be built fully starting from the root.
    
    Returns:
        The root node of the decision tree.
    """
    dt_root = None
    # TODO: finish this.
    # use excel found when A0 <= 0, y = 0; when A0 > 0, A2 <= -0.7045, y = 2; 
    # when A0 > 0, A2 > -0.7045, A3 >= -0.1095, y = 1; when A0 > 0, A2 > -0.7045, A3 < -0.8276, y = 0
    # decision tree like:
    #              A0 <= 0
    #              /    \
    #             /      \
    #            0     A2 <= -0.7045
    #                    /  \
    #                   /    \
    #                  /      \
    #                 2    A3 >= -0.1095
    #                        /  \
    #                       1    0
    func_A0 = lambda feature: feature[0] <= 0
    dt_root = DecisionNode(None,None,func_A0, None)
    dt_root.left = DecisionNode(None,None,None,0)
    
    func_A2 = lambda feature: feature[2] <= -0.7045
    dt_root.right = DecisionNode(None,None,func_A2, None)
    dt_root.right.left = DecisionNode(None,None,None,2)

    func_A3 = lambda feature: feature[3] >= -0.1095
    dt_root.right.right = DecisionNode(None,None,func_A3, None)
    dt_root.right.right.left = DecisionNode(None,None,None,1)
    dt_root.right.right.right = DecisionNode(None,None,None,0)

    return dt_root


def confusion_matrix(true_labels, classifier_output, n_classes=2):
    """Create a confusion matrix to measure classifier performance.
   
    Classifier output vs true labels, which is equal to:
    Predicted  vs  Actual Values.
    
    Output will sum multiclass performance in the example format:
    (Assume the labels are 0,1,2,...n)
                                     |Predicted|
                     
    |A|            0,            1,           2,       .....,      n
    |c|   0:  [[count(0,0),  count(0,1),  count(0,2),  .....,  count(0,n)],
    |t|   1:   [count(1,0),  count(1,1),  count(1,2),  .....,  count(1,n)],
    |u|   2:   [count(2,0),  count(2,1),  count(2,2),  .....,  count(2,n)],'
    |a|   .............,
    |l|   n:   [count(n,0),  count(n,1),  count(n,2),  .....,  count(n,n)]]
    
    'count' function is expressed as 'count(actual label, predicted label)'.
    
    For example, count (0,1) represents the total number of actual label 0 and the predicted label 1;
                 count (3,2) represents the total number of actual label 3 and the predicted label 2.           
    
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
        n_classes: int: number of classes needed due to possible multiple runs with incomplete class sets
    Returns:
        A two dimensional array representing the confusion matrix.
    """
    c_matrix = None
    # TODO: finish this.
    # through n_classes to initialize confusion matrix, 00, 01, 10, 11
    c_matrix = np.zeros((n_classes, n_classes), dtype=int)
    for i in range(len(true_labels)):
        # count the number of actual label and the predicted label
        c_matrix[true_labels[i]][classifier_output[i]] += 1
  
    return c_matrix


def precision(true_labels, classifier_output, n_classes=2, pe_matrix=None):
    """
    Get the precision of a classifier compared to the correct values.
    In this assignment, precision for label n can be calculated by the formula:
        precision (n) = number of correctly classified label n / number of all predicted label n 
                      = count (n,n) / (count(0, n) + count(1,n) + .... + count (n,n))
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
        n_classes: int: number of classes needed due to possible multiple runs with incomplete class sets
        pe_matrix: pre-existing numpy confusion matrix
    Returns:
        The list of precision of each classifier output. 
        So if the classifier is (0,1,2,...,n), the output should be in the below format: 
        [precision (0), precision(1), precision(2), ... precision(n)].
    """
    # TODO: finish this.
    if pe_matrix is None:
        pe_matrix = confusion_matrix(true_labels, classifier_output, n_classes)
    precision_list = np.zeros(n_classes)
    for i in range(n_classes):
        # count (n,n) / (count(0, n) + count(1,n) + .... + count (n,n)) value of count(i,i) / all i column elements
        if np.sum(pe_matrix[:, i]) == 0:
            precision_list[i] = 0
        else:
            precision_list[i] = pe_matrix[i][i] / np.sum(pe_matrix[:, i])
    return precision_list



def recall(true_labels, classifier_output, n_classes=2, pe_matrix=None):
    """
    Get the recall of a classifier compared to the correct values.
    In this assignment, recall for label n can be calculated by the formula:
        recall (n) = number of correctly classified label n / number of all true label n 
                   = count (n,n) / (count(n, 0) + count(n,1) + .... + count (n,n))
    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
        n_classes: int: number of classes needed due to possible multiple runs with incomplete class sets
        pe_matrix: pre-existing numpy confusion matrix
    Returns:
        The list of recall of each classifier output..
        So if the classifier is (0,1,2,...,n), the output should be in the below format: 
        [recall (0), recall (1), recall (2), ... recall (n)].
    """
    # TODO: finish this.
    if pe_matrix is None:
        pe_matrix = confusion_matrix(true_labels, classifier_output, n_classes)
    recall_list = np.zeros(n_classes)
    for i in range(n_classes):
        # count (n,n) / (count(n, 0) + count(n,1) + .... + count (n,n)) value of count(i,i) / all i row elements
        if np.sum(pe_matrix[i, :]) == 0:
            recall_list[i] = 0
        else:
            recall_list[i] = pe_matrix[i][i] / np.sum(pe_matrix[i, :])
    return recall_list


def accuracy(true_labels, classifier_output, n_classes=2, pe_matrix=None):
    """Get the accuracy of a classifier compared to the correct values.
    Balanced Accuracy Weighted:
    -Balanced Accuracy: Sum of the ratios (accurate divided by sum of its row) divided by number of classes.
    -Balanced Accuracy Weighted: Balanced Accuracy with weighting added in the numerator and denominator.

    Args:
        classifier_output (list(int)): output from classifier.
        true_labels: (list(int): correct classified labels.
        n_classes: int: number of classes needed due to possible multiple runs with incomplete class sets
        pe_matrix: pre-existing numpy confusion matrix
    Returns:
        The accuracy of the classifier output.
    """
    # TODO: finish this.
    if pe_matrix is None:
        pe_matrix = confusion_matrix(true_labels, classifier_output, n_classes)
    balance_accuracy = 0
    total = 0
    for i in range(n_classes):
        # sum of the ratios (accurate divided by sum of its row) divided by number of classes
        balance_accuracy += pe_matrix[i][i]
        total += np.sum(pe_matrix[i, :])
    accuracy = balance_accuracy / total
    return accuracy


def gini_impurity(class_vector):
    """Compute the gini impurity for a list of classes.
    This is a measure of how often a randomly chosen element
    drawn from the class_vector would be incorrectly labeled
    if it was randomly labeled according to the distribution
    of the labels in the class_vector.
    It reaches its minimum at zero when all elements of class_vector
    belong to the same class.
    Args:
        class_vector (list(int)): Vector of classes given as 0, 1, 2, ...
    Returns:
        Floating point number representing the gini impurity.
    """
    # TODO: finish this.
    labels, counts = np.unique(class_vector, return_counts=True)
    gini_impurity = 1
    for count in counts:
        # 1 - pi^2
        gini_impurity -= (count / len(class_vector)) ** 2
    return gini_impurity
        


def gini_gain(previous_classes, current_classes):
    """Compute the gini impurity gain between the previous and current classes.
    Args:
        previous_classes (list(int)): Vector of classes given as 0, 1, 2....
        current_classes (list(list(int): A list of lists where each list has
            0, 1, 2, ... values).
    Returns:
        Floating point number representing the gini gain.
    """
    # TODO: finish this.
    gini_prev = gini_impurity(previous_classes)
    total = len(previous_classes)
    gini_curr = 0
    for list in current_classes:
        # calculate the weight of each current class gini impurity
        gini_curr += len(list) / total * gini_impurity(list)
    gini_gain = gini_prev - gini_curr
    return gini_gain

class DecisionTree:
    """Class for automatic tree-building and classification."""

    def __init__(self, depth_limit=22):
        """Create a decision tree with a set depth limit.
        Starts with an empty root.
        Args:
            depth_limit (float): The maximum depth to build the tree.
        """

        self.root = None
        self.depth_limit = depth_limit

    def fit(self, features, classes):
        """Build the tree from root using __build_tree__().
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """

        self.root = self.__build_tree__(features, classes)

    def __build_tree__(self, features, classes, depth=0):
        """Build tree that automatically finds the decision functions.
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
            depth (int): depth to build tree to.
        Returns:
            Root node of decision tree.
        """
        # TODO: finish this.
        # If all input vectors have the same class, return a leaf node with the pappropriate class label.
        # If a specified depth limit is reached, return a leaf labeled with the most frequent class.
        

        if depth >= self.depth_limit or len(set(classes)) == 1 or len(classes) <= 1:
            # if depth is greater than or equal to the depth limit or all classes are the same, return the class
            return DecisionNode(None, None, None, Counter(classes).most_common(1)[0][0])
        # add dimension to classes if needed
        classes = classes[:, np.newaxis]
        # conbine features and classes
        table = np.hstack((features, classes))

        # initialize the best decision function, left and right class, left and right features
        alpha_best = 0
        idx = 0
        threshold = 0
        best_decision_function = None
        best_left_class = None
        best_right_class = None
        best_left_features = None
        best_right_features = None

        for i in range(features.shape[1]):
            # sort the feature values
            sorted_table = table[table[:, i].argsort()]
            if len(sorted_table) % 2 == 0:
                median = (sorted_table[len(sorted_table) // 2 - 1, i] + sorted_table[len(sorted_table) // 2, i]) / 2
            else:
                median = sorted_table[len(sorted_table) // 2, i]
            # split the table into two parts
            left_table = sorted_table[sorted_table[:, i] <= median]
            right_table = sorted_table[sorted_table[:, i] > median]
            # if the left table or right table is empty, continue
            if len(left_table) == 0 or len(right_table) == 0:
                continue
            current_classes = [left_table[:, -1], right_table[:, -1]]
            alpha = gini_gain(classes, current_classes)
            if alpha > alpha_best:
                alpha_best = alpha
                idx = i
                threshold = median
                best_decision_function = lambda feature: feature[idx] <= threshold
                best_left_class = left_table[:, -1]
                best_right_class = right_table[:, -1]
                best_left_features = left_table[:, :-1]
                best_right_features = right_table[:, :-1]
        # stop if the best decision function is None
        if best_decision_function is None:
            _, count = np.unique(classes, return_counts=True)
            return DecisionNode(None, None, None, np.argmax(count))
        left = self.__build_tree__(best_left_features, best_left_class, depth + 1)
        right = self.__build_tree__(best_right_features, best_right_class, depth + 1)
        return DecisionNode(left, right, best_decision_function, None)


    def classify(self, features):
        """Use the fitted tree to classify a list of example features.
        Args:
            features (m x n): m examples with n features.
        Return:
            A list of class labels.
        """
        class_labels = []
        # TODO: finish this.
        for feature in features:
            class_labels.append(self.root.decide(feature))         
        return class_labels


def generate_k_folds(dataset, k):
    """Split dataset into folds.
    Randomly split data into k equal subsets.
    Fold is a tuple (training_set, test_set).
    Set is a tuple (features, classes).
    Args:
        dataset: dataset to be split.
        k (int): number of subsections to create.
    Returns:
        List of folds.
        => Each fold is a tuple of sets.
        => Each Set is a tuple of numpy arrays.
    """
    folds = []
    # TODO: finish this.

#     The general procedure is as follows:

# Shuffle the dataset randomly.
# Split the dataset into k groups
# For each unique group:
# Take the group as a hold out or test data set
# Take the remaining groups as a training data set
# Fit a model on the training set and evaluate it on the test set
# Retain the evaluation score and discard the model
# Summarize the skill of the model using the sample of model evaluation scores
   
    size = len(dataset[0])
    # try to fix only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
    idx = int(size // k)
     # shuffle the dataset randomly, shuffler is the index of the dataset
    shuffler = np.random.permutation(size)
    features, classes = dataset
    features = features[shuffler]
    classes = classes[shuffler]
    # split the dataset into k groups
    for i in range(k):
        # take the group as a hold out or test data set
        start = int(i * idx)
        end = int((i + 1) * idx)
        test_features = features[start : end]
        test_classes = classes[start : end]
        # take the remaining groups as a training data set, use delete to remove the test data
        # try to fix only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices 
        train_features = np.concatenate([features[:start], features[end:]], axis=0)
        train_classes = np.concatenate([classes[:start], classes[end:]], axis=0)
        # fit a model on the training set and evaluate it on the test set
        training_set = (train_features, train_classes)
        testing_set = (test_features, test_classes)
        folds.append((training_set, testing_set))
    return folds


class RandomForest:
    """Random forest classification."""

    def __init__(self, num_trees=200, depth_limit=5, example_subsample_rate=.1,
                 attr_subsample_rate=.3):
        """Create a random forest.
         Args:
             num_trees (int): fixed number of trees.
             depth_limit (int): max depth limit of tree.
             example_subsample_rate (float): percentage of example samples.
             attr_subsample_rate (float): percentage of attribute samples.
        """
        self.trees = []
        self.num_trees = num_trees
        self.depth_limit = depth_limit
        self.example_subsample_rate = example_subsample_rate
        self.attr_subsample_rate = attr_subsample_rate
        # add attributes to store the attributes of each tree
        self.attributes = []

    def fit(self, features, classes):
        """Build a random forest of decision trees using Bootstrap Aggregation.
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """
        # TODO: finish this.
        # columns_feature is the columns of features
        columns_feature = len(features[0])
        # rows_feature is the rows of features
        rows_feature = len(features)
        # number_attrs is the number of attributes
        number_attributes = int(columns_feature * self.attr_subsample_rate)
        # number_example is the number of examples
        number_examples = int(rows_feature * self.example_subsample_rate)

        for _ in range(self.num_trees):
            # randomly select the examples and attributes
            selected_example_idx = np.random.choice(rows_feature, number_examples, replace=False)
            selected_attribute_idx = np.random.choice(columns_feature, number_attributes, replace=False)
            # select the examples and attributes
            selected_example = features[selected_example_idx, :]
            selected_attributes = selected_example[:, selected_attribute_idx]
            selected_class = classes[selected_example_idx]
            # fit the decision tree
            tree = DecisionTree(depth_limit=self.depth_limit)
            tree.fit(selected_attributes,selected_class)
            self.trees.append(tree)
            # print("2222", len(self.trees), "3333", len(self.attributes), "4444", len(selected_attribute_idx), "5555", selected_attribute_idx)
            # store the attributes of each tree, used for classify
            self.attributes.append(selected_attribute_idx)


    def classify(self, features):
            """Classify a list of features based on the trained random forest.
            Args:
                features (m x n): m examples with n features.
            Returns:
                votes (list(int)): m votes for each element
            """
            votes = []
            # TODO: finish this.
            # for each tree, classify the features
            result = [[0] for _ in range(len(features))]
            for i in range(self.num_trees):
                tree = self.trees[i]
                selected_attribute_idx = self.attributes[i]
                # for each tree, classify the features
                selected_attributes = features[:,selected_attribute_idx]
                class_labels = tree.classify(selected_attributes)
                # convert the class labels to numpy array
                class_labels = np.array(class_labels)
                class_labels = class_labels.reshape(-1, 1)
                # store the class labels
                result = np.hstack((result, class_labels))
            # convert each row to int 
            result = result.astype(int)
            for row in result:
                # get the most common class label
                votes.append(Counter(row).most_common(1)[0][0])
            return votes


class ChallengeClassifier:
    """Challenge Classifier used on Challenge Training Data."""

    def __init__(self, n_clf=0, depth_limit=0, example_subsample_rt=0.0, \
                 attr_subsample_rt=0.0, max_boost_cycles=0):
        """Create a boosting class which uses decision trees.
        Initialize and/or add whatever parameters you may need here.
        Args:
             num_clf (int): fixed number of classifiers.
             depth_limit (int): max depth limit of tree.
             attr_subsample_rate (float): percentage of attribute samples.
             example_subsample_rate (float): percentage of example samples.
        """
        self.num_clf = n_clf
        self.depth_limit = depth_limit
        self.example_subsample_rt = example_subsample_rt
        self.attr_subsample_rt=attr_subsample_rt
        self.max_boost_cycles = max_boost_cycles
        # TODO: finish this.
        self.clfs = []
        self.alpha = []
        self.attributes = []



    def fit(self, features, classes):
        """Build the boosting functions classifiers.
            Fit your model to the provided features.
        Args:
            features (m x n): m examples with n features.
            classes (m x 1): Array of Classes.
        """
        # TODO: finish this.
        # columns_feature is the columns of features
        columns_feature = len(features[0])
        # rows_feature is the rows of features
        rows_feature = len(features)
        # number_attrs is the number of attributes
        number_attributes = int(columns_feature * self.attr_subsample_rt)
        # number_example is the number of examples
        number_examples = int(rows_feature * self.example_subsample_rt)
        # initialize the weights
        weights = np.ones(len(classes)) / len(classes)
        for _ in range(self.num_clf):
            # randomly select the examples and attributes
            selected_example_idx = np.random.choice(rows_feature, number_examples, replace=False, p=weights)
            selected_attribute_idx = np.random.choice(columns_feature, number_attributes, replace=False)
            # select the examples and attributes
            selected_example = features[selected_example_idx, :]
            selected_attributes = selected_example[:, selected_attribute_idx]
            selected_class = classes[selected_example_idx]
            # fit the decision tree
            tree = DecisionTree(depth_limit=self.depth_limit)
            tree.fit(selected_attributes,selected_class)
            self.clfs.append(tree)
            # store the attributes of each tree, used for classify
            self.attributes.append(selected_attribute_idx)
            # calculate the error
            error = 0
            for i in range(len(features)):
                if tree.classify(features[i][selected_attribute_idx]) != classes[i]:
                    error += weights[i]
            # calculate the alpha
            alpha = 0.5 * np.log((1 - error) / error)
            self.alpha.append(alpha)
            # update the weights
            for i in range(len(features)):
                if tree.classify(features[i][selected_attribute_idx]) == classes[i]:
                    weights[i] *= np.exp(-alpha)
                else:
                    weights[i] *= np.exp(alpha)
            weights /= np.sum(weights)


    def classify(self, features):
        """Classify a list of features.
        Predict the labels for each feature in features to its corresponding class
        Args:
            features (m x n): m examples with n features.
        Returns:
            A list of class labels.
        """
        # TODO: finish this.
        votes = []
        result = [[0] for _ in range(len(features))]
        for i in range(self.num_clf):
            tree = self.clfs[i]
            selected_attribute_idx = self.attributes[i]
            # for each tree, classify the features
            selected_attributes = features[:,selected_attribute_idx]
            class_labels = tree.classify(selected_attributes)
            # convert the class labels to numpy array
            class_labels = np.array(class_labels)
            class_labels = class_labels.reshape(-1, 1)
            # store the class labels
            result = np.hstack((result, class_labels))
        # convert each row to int
        result = list(map(int, result))
        for row in result:
            # get the most common class label
            votes.append(Counter(row).most_common(1)[0][0])
        return votes


class Vectorization:
    """Vectorization preparation for Assignment 5."""

    def __init__(self):
        pass

    def non_vectorized_loops(self, data):
        """Element wise array arithmetic with loops.
        This function takes one matrix, multiplies by itself and then adds to
        itself.
        Args:
            data: data to be added to array.
        Returns:
            Numpy array of data.
        """

        non_vectorized = np.zeros(data.shape)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                non_vectorized[row][col] = (data[row][col] * data[row][col] +
                                            data[row][col])
        return non_vectorized

    def vectorized_loops(self, data):
        """Array arithmetic using vectorization.
        This function takes one matrix, multiplies by itself and then adds to
        itself.
        Args:
            data: data to be sliced and summed.
        Returns:
            Numpy array of data.
        """
        # TODO: finish this.
        vectorized = data * data + data
        return vectorized

    def non_vectorized_slice(self, data):
        """Find row with max sum using loops.
        This function searches through the first 100 rows, looking for the row
        with the max sum. (ie, add all the values in that row together).
        Args:
            data: data to be added to array.
        Returns:
            Tuple (Max row sum, index of row with max sum)
        """
        max_sum = 0
        max_sum_index = 0
        for row in range(100):
            temp_sum = 0
            for col in range(data.shape[1]):
                temp_sum += data[row][col]

            if temp_sum > max_sum:
                max_sum = temp_sum
                max_sum_index = row

        return (max_sum, max_sum_index)

    def vectorized_slice(self, data):
        """Find row with max sum using vectorization.
        This function searches through the first 100 rows, looking for the row
        with the max sum. (ie, add all the values in that row together).
        Args:
            data: data to be sliced and summed.
        Returns:
            Tuple (Max row sum, index of row with max sum)
        """
        # TODO: finish this.
        slice_data = data[:100]
        # axis = 1 sums the rows
        max_sum = np.sum(slice_data, axis=1)
        max_sum_index = np.argmax(max_sum)
        return (max_sum[max_sum_index], max_sum_index)

    def non_vectorized_flatten(self, data):
        """Display occurrences of positive numbers using loops.
         Flattens down data into a 1d array, then creates a dictionary of how
         often a positive number appears in the data and displays that value.
         ie, [(1203,3)] = integer 1203 appeared 3 times in data.
         Args:
            data: data to be added to array.
        Returns:
            Dictionary [(integer, number of occurrences), ...]
        """
        unique_dict = {}
        flattened = data.flatten()
        for item in flattened:
            if item > 0:
                if item in unique_dict:
                    unique_dict[item] += 1
                else:
                    unique_dict[item] = 1

        return unique_dict.items()

    def vectorized_flatten(self, data):
        """Display occurrences of positive numbers using vectorization.
         Flattens down data into a 1d array, then creates a dictionary of how
         often a positive number appears in the data and displays that value.
         ie, [(1203,3)] = integer 1203 appeared 3 times in data.
         Args:
            data: data to be added to array.
        Returns:
            Dictionary [(integer, number of occurrences), ...]
        """
        # TODO: finish this.
        # item ia new array with positive values
        item = data[data > 0]
        # ar: item will be flattened, return_counts: count of each unique element
        # unique and count are arrays
        unique, count = np.unique(item, return_counts=True)
        # convert unique and count to dictionary, then convert to items, like non_vectorized_flatten return format
        return dict(zip(unique, count)).items()

    def non_vectorized_glue(self, data, vector, dimension='c'):
        """Element wise array arithmetic with loops.
        This function takes a multi-dimensional array and a vector, and then combines
        both of them into a new multi-dimensional array. It must be capable of handling
        both column and row-wise additions.
        Args:
            data: multi-dimensional array.
            vector: either column or row vector
            dimension: either c for column or r for row
        Returns:
            Numpy array of data.
        """
        if dimension == 'c' and len(vector) == data.shape[0]:
            non_vectorized = np.ones((data.shape[0],data.shape[1]+1), dtype=float)
            non_vectorized[:, -1] *= vector
        elif dimension == 'r' and len(vector) == data.shape[1]:
            non_vectorized = np.ones((data.shape[0]+1,data.shape[1]), dtype=float)
            non_vectorized[-1, :] *= vector
        else:
            raise ValueError('This parameter must be either c for column or r for row')
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                non_vectorized[row, col] = data[row, col]
        return non_vectorized

    def vectorized_glue(self, data, vector, dimension='c'):
        """Array arithmetic without loops.
        This function takes a multi-dimensional array and a vector, and then combines
        both of them into a new multi-dimensional array. It must be capable of handling
        both column and row-wise additions.
        Args:
            data: multi-dimensional array.
            vector: either column or row vector
            dimension: either c for column or r for row
        Returns:
            Numpy array of data.
        """
        vectorized = None
        # column stack and row stack is ok since we could treat the data as 1D array
        # we also could use np.hstack and np.vstack
        if dimension == 'c' and len(vector) == data.shape[0]:
            vectorized = np.column_stack((data, vector))
        elif dimension == 'r' and len(vector) == data.shape[1]:
            vectorized = np.row_stack((data, vector))
        else:
            raise ValueError('This parameter must be either c for column or r for row')
        return vectorized

    def non_vectorized_mask(self, data, threshold):
        """Element wise array evaluation with loops.
        This function takes a multi-dimensional array and then populates a new
        multi-dimensional array. If the value in data is below threshold it
        will be squared.
        Args:
            data: multi-dimensional array.
            threshold: evaluation value for the array if a value is below it, it is squared
        Returns:
            Numpy array of data.
        """
        non_vectorized = np.zeros_like(data, dtype=float)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                val = data[row, col]
                if val >= threshold:
                    non_vectorized[row, col] = val
                    continue
                non_vectorized[row, col] = val**2

        return non_vectorized

    def vectorized_mask(self, data, threshold):
        """Array evaluation without loops.
        This function takes a multi-dimensional array and then populates a new
        multi-dimensional array. If the value in data is below threshold it
        will be squared. You are required to use a binary mask for this problem
        Args:
            data: multi-dimensional array.
            threshold: evaluation value for the array if a value is below it, it is squared
        Returns:
            Numpy array of data.
        """
        vectorized = None
        mask = data < threshold
        # condition is True, then use data**2, otherwise use data
        vectorized = np.where(mask, data**2, data)
        return vectorized


def return_your_name():
    # return your name
    # TODO: finish this
    
    return 'Jing Li'
