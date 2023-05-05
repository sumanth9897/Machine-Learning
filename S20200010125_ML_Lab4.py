from csv import reader
import random
from collections import defaultdict

def fileReader(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csvReader = reader(file)
		for row in csvReader:
			if not row:
				continue
			dataset.append(row)
	return dataset

dataset = fileReader("iris.data")

for i in range(len(dataset)):
    for j in range(4):
        dataset[i][j] = float(dataset[i][j])

for i in range(len(dataset)):
    # match dataset[i][4]:
    #     case 'Iris-setosa': dataset[i][4] = 0
    #     case 'Iris-versicolor': dataset[i][4] = 1
    #     case 'Iris-virginica': dataset[i][4] = 2   
    if dataset[i][4]=='Iris-setosa':
        dataset[i][4] = 0
    elif dataset[i][4]=='Iris-versicolor':
        dataset[i][4] = 1
    else:
        dataset[i][4] = 2


dataset_disc = []
for i in range(len(dataset)):
    temp = []
    for j in range(4):
        temp.append(round(dataset[i][j]))
    temp.append(dataset[i][4])
    dataset_disc.append(temp)    

min_sepal_len = min(i[0] for i in dataset_disc)
max_sepal_len = max(i[0] for i in dataset_disc)
len_sepl = max_sepal_len - min_sepal_len + 1

min_sepal_width = min(i[1] for i in dataset_disc)
max_sepal_width = max(i[1] for i in dataset_disc)
len_sepw = max_sepal_width - min_sepal_width + 1

min_petal_len = min(i[2] for i in dataset_disc)
max_petal_len = max(i[2] for i in dataset_disc)
len_petl = max_petal_len - min_petal_len + 1

min_petal_width = min(i[3] for i in dataset_disc)
max_petal_width = max(i[3] for i in dataset_disc)
len_petw = max_petal_width - min_petal_width + 1

random.shuffle(dataset_disc)
disc_TrainData = dataset_disc[:120]
disc_TestData = dataset_disc[120:]

sepal_len_0 = defaultdict(int)
sepal_len_1 = defaultdict(int)
sepal_len_2 = defaultdict(int)

sepal_wid_0 = defaultdict(int)
sepal_wid_1 = defaultdict(int)
sepal_wid_2 = defaultdict(int)

petal_len_0 = defaultdict(int)
petal_len_1 = defaultdict(int)
petal_len_2 = defaultdict(int)

petal_wid_0 = defaultdict(int)
petal_wid_1 = defaultdict(int)
petal_wid_2 = defaultdict(int)
for row in disc_TrainData:
    # match row[4]:
    #     case 0: 
    #         sepal_len_0[row[0]] += 1
    #         sepal_wid_0[row[1]] += 1
    #         petal_len_0[row[2]] += 1
    #         petal_wid_0[row[3]] += 1
    #     case 1:
    #         sepal_len_1[row[0]] += 1
    #         sepal_wid_1[row[1]] += 1
    #         petal_len_1[row[2]] += 1
    #         petal_wid_1[row[3]] += 1
    #     case 2: 
    #         sepal_len_2[row[0]] += 1
    #         sepal_wid_2[row[1]] += 1
    #         petal_len_2[row[2]] += 1
    #         petal_wid_2[row[3]] += 1
    
    if row[4]==0:
        sepal_len_0[row[0]] += 1
        sepal_wid_0[row[1]] += 1
        petal_len_0[row[2]] += 1
        petal_wid_0[row[3]] += 1
    elif row[4]==1:
            sepal_len_1[row[0]] += 1
            sepal_wid_1[row[1]] += 1
            petal_len_1[row[2]] += 1
            petal_wid_1[row[3]] += 1
    else:
            sepal_len_2[row[0]] += 1
            sepal_wid_2[row[1]] += 1
            petal_len_2[row[2]] += 1
            petal_wid_2[row[3]] += 1       


SL = [[0 for _ in range(3)] for _ in range(len_sepl)]
SW = [[0 for _ in range(3)] for _ in range(len_sepw)]
PL = [[0 for _ in range(3)] for _ in range(len_petl)]
PW = [[0 for _ in range(3)] for _ in range(len_petw)]

for i in range(len_sepl):
    SL[i][0] = sepal_len_0[min_sepal_len+i]
    SL[i][1] = sepal_len_1[min_sepal_len+i]
    SL[i][2] = sepal_len_2[min_sepal_len+i]

for i in range(len_sepw):
    SW[i][0] = sepal_wid_0[min_sepal_width+i]
    SW[i][1] = sepal_wid_1[min_sepal_width+i]
    SW[i][2] = sepal_wid_2[min_sepal_width+i]

for i in range(len_petl):
    PL[i][0] = petal_len_0[min_petal_len+i]
    PL[i][1] = petal_len_1[min_petal_len+i]
    PL[i][2] = petal_len_2[min_petal_len+i]

for i in range(len_petw):
    PW[i][0] = petal_wid_0[min_petal_width+i]
    PW[i][1] = petal_wid_1[min_petal_width+i]
    PW[i][2] = petal_wid_2[min_petal_width+i]

col1 = sum([i[0] for i in SL])
col2 = sum([i[1] for i in SL])
col3 = sum([i[2] for i in SL])
SL.append([col1, col2, col3])

col1 = sum([i[0] for i in SW])
col2 = sum([i[1] for i in SW])
col3 = sum([i[2] for i in SW])
SW.append([col1, col2, col3])

col1 = sum([i[0] for i in PL])
col2 = sum([i[1] for i in PL])
col3 = sum([i[2] for i in PL])
PL.append([col1, col2, col3])

col1 = sum([i[0] for i in PW])
col2 = sum([i[1] for i in PW])
col3 = sum([i[2] for i in PW])
PW.append([col1, col2, col3])


cnt = 0
for row in disc_TestData:
    tempSL = row[0]
    tempSW = row[1]
    tempPL = row[2]
    tempPW = row[3]
    try:
        probSL0 = (SL[tempSL - min_sepal_len][0])/SL[len_sepl][0]
        probSW0 = (SW[tempSW - min_sepal_width][0])/SW[len_sepw][0]
        probPL0 = (PL[tempPL - min_petal_len][0])/PL[len_petl][0]
        probPW0 = (PW[tempPW - min_petal_width][0])/PW[len_petw][0]
    except ZeroDivisionError:
        probSL0=0
        probSW0=0
        probPL0=0
        probPW0=0

    # probSL0 = (SL[tempSL - min_sepal_length][0])/SL[len_sepl][0]
    # probSW0 = (SW[tempSW - min_sepal_width][0])/SW[len_sepw][0]
    # probPL0 = (PL[tempPL - min_petal_length][0])/PL[len_petl][0]
    # probPW0 = (PW[tempPW - min_petal_width][0])/PW[len_petw][0]
    prob0 = probSL0 * probSW0 * probPL0 * probPW0
    try:
        probSL1 = (SL[tempSL - min_sepal_len][1])/SL[len_sepl][1]
        probSW1 = (SW[tempSW - min_sepal_width][1])/SW[len_sepw][1]
        probPL1 = (PL[tempPL - min_petal_len][1])/PL[len_petl][1]
        probPW1 = (PW[tempPW - min_petal_width][1])/PW[len_petw][1]
    except:
        probSL1=0
        probSW1=0
        probPL1=0
        probPW1=0       

    # probSL1 = (SL[tempSL - min_sepal_length][1])/SL[len_sepl][1]
    # probSW1 = (SW[tempSW - min_sepal_width][1])/SW[len_sepw][1]
    # probPL1 = (PL[tempPL - min_petal_length][1])/PL[len_petl][1]
    # probPW1 = (PW[tempPW - min_petal_width][1])/PW[len_petw][1]
    prob1 = probSL1 * probSW1 * probPL1 * probPW1
    try:
        probSL2 = (SL[tempSL - min_sepal_len][2])/SL[len_sepl][2]
        probSW2 = (SW[tempSW - min_sepal_width][2])/SW[len_sepw][2]
        probPL2 = (PL[tempPL - min_petal_len][2])/PL[len_petl][2]
        probPW2 = (PW[tempPW - min_petal_width][2])/PW[len_petw][2]
    except:
        probSL2=0
        probSW2=0
        probPL2=0
        probPW2=0         

    # probSL2 = (SL[tempSL - min_sepal_length][2])/SL[len_sepl][2]
    # probSW2 = (SW[tempSW - min_sepal_width][2])/SW[len_sepw][2]
    # probPL2 = (PL[tempPL - min_petal_length][2])/PL[len_petl][2]
    # probPW2 = (PW[tempPW - min_petal_width][2])/PW[len_petw][2]
    prob2 = probSL2 * probSW2 * probPL2 * probPW2


    label = 2
    if (prob0 > prob1) and (prob0 > prob2): label = 0
    elif (prob1 > prob0) and (prob1 > prob2): label = 1

    if label == row[4]: cnt+=1

print('Accuracy is ',((cnt/30) * 100),'%')