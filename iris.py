# Implement k-Nearest Neighbor Classifier over the Iris Data



# 1. Implement 1-NNC
# 2. Implement 3-NNC
# 3. Divide the data into the training data and the test data (randomly divide the data in to 120 training examples and 30 test examples)
# 4. Report accuracy of the 1-NNC, and k-NNC over the test data.


from csv import reader
from math import sqrt
import random


def load_csv(file_name):
	dataset = list()
	with open(file_name, 'r') as file1:
		csv_reader = reader(file1)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 

def str_column_to_float(dataset, column1):
	for row in dataset:
		row[column1] = float(row[column1].strip())
 

def str_column_to_int(dataset, col):
	class_values = [row[col] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[col] = lookup[row[col]]
	return lookup
 

def dataset_minmax(datasett):
	minmax = list()
	for i in range(len(datasett[0])):
		col_values = [row[i] for row in datasett]
		valu_min = min(col_values)
		valu_max = max(col_values)
		minmax.append([valu_min, valu_max])
	return minmax
 

def normalize_dataset(datasett, minmax1):
	for row in datasett:
		for i in range(len(row)):
			row[i] = (row[i] - minmax1[i][0]) / (minmax1[i][1] - minmax1[i][0])
 

def euclidean_distance(row_1, row_2):
	distance = 0.0
	for i in range(len(row_1)-1):
		distance += (row_1[i] - row_2[i])**2
	return sqrt(distance)
 

def get_neighbors(train, test_row, num_neighbours):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbours = list()
	for i in range(num_neighbours):
		neighbours.append(distances[i][0])
	return neighbours
 

def predict_classification(train, test_row, num_neighbours):
	neighbours = get_neighbours(train, test_row, num_neighbours)
	output_values = [row[-1] for row in neighbours]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 

file_name = 'Iris.data'
dataset = load_csv(file_name)


num_neighbors = 3

dataset = load_csv("iris.data")
dataset_30 = random.sample(dataset, 30)



dataset_120 = [i for i in dataset if i not in dataset_30 ]
for i in range(len(dataset_30[0])-1):
	str_column_to_float(dataset_30, i)

str_column_to_int(dataset_30, len(dataset_30[0])-1)

for i in range(len(dataset_120[0])-1):
	str_column_to_float(dataset_120, i)

str_column_to_int(dataset_120, len(dataset_120[0])-1)

for i in dataset_30:
 label = predict_classification(dataset_120, i, num_neighbors)
 print('Data=%s, Predicted: %s' % (i, label))