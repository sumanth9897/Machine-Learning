
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.random.randint(60,360,size=240)
X_1 = []   
for i in range(len(x)):
    X_1.append(math.radians(x[i])) 

K = np.random.normal(0.5, 0.15)  
output = []
for i in range(len(X_1)):
    output.append(math.sin(X_1[i])+math.cos(X_1[i]) + K**2)

DataSet = []

for i in range(len(x)):
    DataSet.append([X_1[i],output[i]])  

DataSet = np.array(DataSet)
np.random.shuffle(DataSet)

testset = DataSet[int(len(DataSet)*0.85):]
print(len(testset))
DataSet = DataSet[:int(len(DataSet)*0.85)]
print(len(DataSet))

def grad_des(x, y, alpha, epochs):
    
    m = np.shape(x)[0] # samples
    n = np.shape(x)[1] # features
    
    x = np.concatenate((np.ones((m,1)),x), axis=1)
    w = 2*np.random.rand(n+1,)-1
    loss_history = []
    
    for current_iteration in range(epochs):
        y_estimated = w.dot(x.T)
        error = y_estimated - y
        cost = np.sum(error ** 2)
        gradient = (1 / m) * x.T.dot(error)
        w = w - alpha * gradient
        loss_history.append(cost)
    return loss_history, w

loss, w = grad_des(DataSet[:,:-1],DataSet[:,-1], 0.01, 100)

plt.figure(facecolor='blue')
ax = plt.axes()
ax.set_facecolor("white")
plt.plot(np.arange(len(loss)), loss)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show

plt.figure(facecolor='blue')
ax = plt.axes()
ax.set_facecolor('white')
for i in range(len(DataSet)):
        plt.plot(DataSet[i,0], DataSet[i,1], 'g.')
for i in range(50):
        plt.plot(i/10, w[1] * i/10 + w[0], 'r+')
plt.show()

def grad_des_n(x, y, alpha, epochs,k):
    
    temp = x
    x = np.concatenate((np.power(x,0),x), axis=1)
    for i in range(1,k):
        x = np.concatenate((x,np.power(temp,i+1)), axis=1)
        
    m = np.shape(x)[0] # samples
    n = np.shape(x)[1] # features
    
    w = 2*np.random.rand(n,)-1
    loss_history = []
    
    for current_iteration in range(epochs):
        y_estimated = w.dot(x.T)
        error = y_estimated - y
        cost = np.sum(error ** 2)
        gradient = (1 / m) * x.T.dot(error)
        w = w - alpha * gradient/(np.linalg.norm(gradient))
        loss_history.append(cost)
    return loss_history, w

def plot_n(DataSet,w,k):
    plt.figure(facecolor='blue')
    ax = plt.axes()
    ax.set_facecolor('white')
    for i in range(len(DataSet)):
            plt.plot(DataSet[i,0], DataSet[i,1], 'g.')

    
    for i in range(100,500):
        data = w[0]
        for j in range(1,k+1):
            data += (w[j] * (i/100)**j)
        plt.plot(i/100, data, 'r+')
    plt.show()

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,1)
print(loss[-1], w)
plot_n(DataSet,w,1)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,3)
print(loss[-1], w)
plot_n(DataSet,w,3)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,13)
print(loss[-1], w)
plot_n(DataSet,w,13)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,15)
print(loss[-1], w)
plot_n(DataSet,w,15)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,1)
print(loss[-1], w)
plot_n(DataSet,w,1)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,5)
print(loss[-1], w)
plot_n(DataSet,w,5)

loss, w = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,15)
print(loss[-1], w)
plot_n(DataSet,w,15)

loss, w_19 = grad_des_n(DataSet[:,:-1],DataSet[:,-1], 0.01, 500,19)
print(loss[-1], w)
plot_n(DataSet,w_19,19)

# test set predictions
k = 19
x = testset[:,:-1]
temp = x
x = np.concatenate((np.power(x,0),x), axis=1)
for i in range(1,k):
        x = np.concatenate((x,np.power(temp,i+1)), axis=1)
print("Test set predictions:")
print(w_19.dot(x.T))

def grad_des_n_l2(x, y, alpha, epochs,k, l):
    
    temp = x
    x = np.concatenate((np.power(x,0),x), axis=1)
    for i in range(1,k):
        x = np.concatenate((x,np.power(temp,i+1)), axis=1)
        
    m = np.shape(x)[0] # samples
    n = np.shape(x)[1] # features
    
    w = 2*np.random.rand(n,)-1
    loss_history = []
    
    for current_iteration in range(epochs):
        y_estimated = w.dot(x.T)
        error = y_estimated - y
        cost = np.sum(error ** 2)
        gradient = (1 / m) * x.T.dot(error)
        w = w - alpha * (gradient/(np.linalg.norm(gradient)) + l*w*w)
        loss_history.append(cost)
    return loss_history, w

l = [1e-10,1e-5]


loss, w = grad_des_n_l2(DataSet[:,:-1],DataSet[:,-1], 0.01, 50,19,l[0])
print(loss[-1], w)
plot_n(DataSet,w,19)

loss, w = grad_des_n_l2(DataSet[:,:-1],DataSet[:,-1], 0.01, 50,19,l[1])
print(loss[-1], w)
plot_n(DataSet,w,19)

l = [1e-10,1e-5]


loss, w_15_1 = grad_des_n_l2(DataSet[:,:-1],DataSet[:,-1], 0.01, 100,15,l[0])
print(loss[-1], w)
plot_n(DataSet,w,15)

loss, w_15_2 = grad_des_n_l2(DataSet[:,:-1],DataSet[:,-1], 0.01, 100,15,l[1])
print(loss[-1], w)
plot_n(DataSet,w,15)

# test set predictions
k = 15
x = testset[:,:-1]
temp = x
x = np.concatenate((np.power(x,0),x), axis=1)
for i in range(1,k):
        x = np.concatenate((x,np.power(temp,i+1)), axis=1)
print("Test set predictions:")
print(w_15_1.dot(x.T))

# test set predictions
k = 15
x = testset[:,:-1]
temp = x
x = np.concatenate((np.power(x,0),x), axis=1)
for i in range(1,k):
        x = np.concatenate((x,np.power(temp,i+1)), axis=1)
print("Test set predictions:")
print(w_15_2.dot(x.T))

print(testset[:,-1])