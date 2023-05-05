from csv import reader
import random
import numpy as np
import statistics 

# function to read csv file
def load(filename):
    data = list()
    with open(filename, 'r') as file:
        csv = reader(file)
        for row in csv:
            if not row:
                continue
            data.append(row)
    return data

# loading data from csv file
data = load('House Price.csv')
data.pop(0)
data = np.array(data)
data = data.astype(np.float64)
a = []
b = []

# ratio division 70:30
for i in range(506):
    if (i<354):
        a.append(data[i])
    else:
        b.append(data[i])

#generating random 12 values in a list 
theta=np.random.random_sample(size=12)

 
def trainset(a,theta):
    for k in range(1):
      x=[]
      for i in range(354):
         y=1
         for j in range(12):
           if(j==0):
             y=theta[j]
           else:
             y+=(a[i][j-1]*theta[j])
         yc=y-a[i][11]
         x.append(yc)
      p=[]
      for i in range(12):
        y=1
        alpha=0.01
        for j in range(354):
           if(i==0):
             y+=x[j]
           else:
             y+=(a[j][i-1]*x[j])
        p.append👍
      for i in range(len(p)):
         p[i]*=(2*0.01)
      q=[]
      for i in range(12):
         q.append(theta[i]-p[i])
      theta=q
    return theta
# trainset operation      
testtheta=trainset(a,theta)

def testset(testtheta,b):
  x=[]
  for i in range(len(b)):
    y=1
    for j in range(len(testtheta)):
      if(j==0):
         y=testtheta[j]
      else:
         y+=(b[i][j-1]*testtheta[j])
    x.append👍
  return x
  
# testset operation      
output=testset(testtheta,b)
print(output)

#MSE
def mse(output,b):
  result=0
  for i in range(152):
    result+=((b[i][11]-output[i])**2)
  print(result/152)
  return result


#MAE
def mae(output,b):
  result=0
  for i in range(152):
    result+=(abs(b[i][11]-output[i]))
  print(result/152)


#R square
def Rsquare(output,b,mse):
  a=[]
  for i in range(152):
    a.append(b[i][11])
  avg=statistics.mean(a)
  result=0
  for i in range(152):
    result+=((b[i][11]-avg)**2)
  print(1-(mse//result))

#operations 
Mse=mse(output,b)
mae(output,b)
Rsquare(output,b,Mse)