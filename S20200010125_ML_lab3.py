from random import seed
from random import randrange
from csv import reader
from math import sqrt
import random
import statistics
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split


def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

 

def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)
 
def k_nearest_neighbors(train, test, num_neighbors):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbors)
		predictions.append(output)
	return(predictions)
 

 
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 

seed(1)
filename = 'pp_traii.dat'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
str_column_to_int(dataset, len(dataset[0])-1)

n_folds =3
# num_neighbors = 5
 
datasetval = random.sample(dataset, 290)
datasetTr = [i for i in dataset if i not in datasetval ]
for i in range(len(datasetval[0])-1):
	str_column_to_float(datasetval, i)

str_column_to_int(datasetval, len(datasetval[0])-1)

for i in range(len(datasetTr[0])-1):
	str_column_to_float(dataset, i)

str_column_to_int(datasetTr, len(datasetTr[0])-1)

s1=[]
s2=[]
s3=[]

cNN=20
for i in range(cNN):
 scores = evaluate_algorithm(datasetTr, k_nearest_neighbors, n_folds, cNN)
#  print('Scores: %s' % scores)
 print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
 add=sum(scores)/float(len(scores))
 s1.append(add)

print("-----------")

datasetval2 = random.sample(datasetTr, 290)
datasetTr2 = [i for i in dataset if i not in datasetval2 ]

for i in range(cNN):
 scores2 = evaluate_algorithm(datasetTr2, k_nearest_neighbors, n_folds, cNN)
 print('Mean Accuracy: %.3f%%' % (sum(scores2)/float(len(scores))))
 add=sum(scores2)/float(len(scores))
 s2.append(add)

print("-----------")

datasetex3 = [i for i in datasetTr2 if i not in datasetval]
datasetval3 = random.sample(datasetex3, 200)
datasetTr3 = [i for i in dataset if i not in datasetval3]

for i in range(cNN):
 scores3 = evaluate_algorithm(datasetTr3, k_nearest_neighbors, n_folds, cNN)
#  print('Scores: %s' % scores)
 print('Mean Accuracy: %.3f%%' % (sum(scores3)/float(len(scores))))
 add=sum(scores3)/float(len(scores))
 s3.append(add)

 dev = []
for i in range(20):
 d = statistics.stdev([s1[i],s2[i],s3[i]])
 dev.append(d)
 print(d)
print(dev.index(min(dev))+1)

datasetThirty=load_csv('test.data')
dataset_new = []

for i in range(len(datasetThirty[0])-1):
	str_column_to_float(datasetThirty, i)
# convert class column to integers
str_column_to_int(dataset, len(datasetThirty[0])-1)
for i in datasetThirty:
 label = predict_classification(dataset, i, 9)
#  print('Data=%s, Predicted: %s' % (i, label))
 temp = i[:4]
 temp.append(label)
 dataset_new.append(temp)

cnt = 0
for i in range(len(datasetThirty)):
	if datasetThirty[i][4]==dataset_new[i][4]: cnt += 1

print(f"Final accuracy is {(cnt/30)*100}")