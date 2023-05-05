from csv import reader
import math
import random
import numpy
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
#Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

dataset = load_csv('heart.csv')
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)

str_column_to_int(dataset, len(dataset[0])-1)

testSet=random.sample(dataset,311)

trainSet=[i for i in dataset if i not in testSet]

class0=[]
for row in trainSet:
    if row[13]==0:
        class0.append(row)


class1=[i for i in trainSet if i not in class0]

meanList=[]
deviationList=[]

meanList0=[]
a0 = numpy.array(class0)
arrMean=numpy.mean(a0,axis=0)
arr=numpy.std(a0,axis=0)
devList0=arr.tolist()
meanList0=arrMean.tolist()


meanList1=[]
a1 = numpy.array(class1)
arrMean1=numpy.mean(a1,axis=0)
arr1=numpy.std(a1,axis=0)
devList1=arr1.tolist()
meanList1=arrMean1.tolist()

pr0 = 1
class0Pro=[]
for row in class0:
    for i in range(13):
        power =math.exp(-(math.pow(row[i]-meanList0[i],2)/(2*math.pow(devList0[i],2))))
        probability= (1 / (math.sqrt(2*math.pi) *devList0[i])) * power
        pr0= pr0 * probability
        class0Pro.append(pr0)

pr1=1
class1Pro=[]
for row in class1:
    for i in range(13):
        power =math.exp(-(math.pow(row[i]-meanList1[i],2)/(2*math.pow(devList1[i],2))))
        probability= (1 / (math.sqrt(2*math.pi) *devList1[i])) * power
        pr1= pr1 * probability
        class1Pro.append(pr1)
# print(class1Pro)

for i in range(311):
    if class0Pro[i]>class1Pro[i]:
        testSet[i].append(0)
    else:
       testSet[i].append(1)

count=0
for row in testSet:
    if row[13]==row[14]:
        count=count+1

print((count/313)*100)
