import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import statistics
import math

def knn(testSet,trainset):
    p=0
    q=0
    for i in range(len(trainset)):
       dist=(((testSet[0]-trainset[i][0])*2+(testSet[1]-trainset[i][1])2)*(1/2))
       if(i==0 ):
         p=dist
         q=trainset[i][2]
       if(dist<p):
          p=dist
          q=trainset[i][2]
    return q

def find_y(testset):
 m1 = np.array([0,0])
 m2 = np.array([0,2])   
 Bayes_prediction = []
 for item in testset:
    x = np.array([float(item[0]),float(item[1])])
    mat1 = x - m1
    mat2 = x - m2
    val1 = (-1/2)*(mat1.dot(mat1.T))
    val2 = (-1/2)*(mat2.dot(mat2.T))
    val1 =(math.exp(val1))
    val2 =(math.exp(val2))
    if val1 >=val2:
        Bayes_prediction.append('1')
    else:
        Bayes_prediction.append('2')
 return Bayes_prediction

mean1 = [0,0]
cov_var1 = [[1, 0], [0,1]]
#class1
mean2 = [0,2]
cov_var2 = [[1, 0], [0,1]]
#class2

trainSet=[]
for i in range(10):
    arr1 = np.random.multivariate_normal(mean1, cov_var1, 50)
    arr2 = np.random.multivariate_normal(mean2, cov_var2, 50)
    zeros = np.zeros((50,1),dtype=float)
    one = np.ones((50,1),dtype=float)
    arr1 = np.append(arr1,zeros,axis=1)
    arr2 = np.append(arr2,one,axis=1)
    temp = np.concatenate((arr1,arr2),axis=0)
    trainSet.append(temp)
testSet=[]
class1 = np.random.multivariate_normal(mean1,cov_var1, 50)
class2 = np.random.multivariate_normal(mean2,cov_var2, 50)
testSet=np.concatenate((class1,class2),axis = 0)
bias=[]
var=[]
c=find_y(testSet)
for i in range(100):
  a=[]
  for j in range(10):
     a.append(knn(testSet[i],trainSet[j]))
  m=max(set(a),key=a.count)
  y=c[i]
  if(float(y)==float(m)):
    bias.append(0)
  else:
    bias.append(1)
  key=0
  for i in range(len(a)):
    if(m!=a[i]):
      key+=1
  var.append(key/10)
print(statistics.mean(bias))
print(statistics.mean(var))