import numpy as np
import matplotlib.pyplot as plt
import copy
import load_mnist
from PIL import Image

# --------------------------------
# Activation
def sigmoid(input):
    x = copy.deepcopy(input)
    return 1 / (1 + np.exp(-x))

def step(input):
    x = copy.deepcopy(input)
    x[x>0] = 1
    x[x<=0] = 0
    return x

def step_function(input):
    return np.array(x>0, dtype=np.int)

def relu(input):
    x = copy.deepcopy(input)
    return np.maximum(0, x)

def softmax(input):
    x = copy.deepcopy(input)
    max_x = np.max(x)
    exp_x = np.exp(x - max_x)
    return exp_x / np.sum(exp_x)

def showActivation():
    x = np.arange(-6,6,0.1)
    plt.plot(x,sigmoid(x),label="sigmoid")
    plt.plot(x,step(x),label="step")
    #plt.plot(x,step_function(x),label="step_function")
    plt.plot(x,relu(x),label="relu")
    plt.xlabel("x")
    plt.ylabel("value")
    plt.ylim(-0.1, 1.1)
    plt.title("Activation Functions")
    plt.legend()
    plt.show()
# --------------------------------

# input2 3 2 output2
def _init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
    network['b1'] = np.array([0.1, 0.1, 0.1])
    network['W2'] = np.array([[0.1, 0.2],[0.3, 0.4],[0.5, 0.6]])
    network['b2'] = np.array([0.1, 0.1])
    network['W3'] = np.array([[0.1, 0.2],[0.3, 0.4]])
    network['b3'] = np.array([0.1, 0.1])

    return network

# any shape network
# network_size = (input, hidden1, ... , output)
def init_network(network_size):
    network = {}
    for i in range(1, len(network_size)):
        weight_name = 'W' + str(i)
        bias_name = 'b' + str(i)
        network[weight_name] = np.random.rand(network_size[i-1], network_size[i])
        network[bias_name] = np.random.rand(network_size[i])
        #print(network[weight_name])
        #print(network[bias_name])

    return network
# --------------------------------

def identity_function(input):
    return softmax(input)
# --------------------------------
def _forward_propagation(network, input):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(input, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3

    y = identity_function(a3)

    return y


def forward_propagation(network, input):
    z = input
    for i in range(0,len(network),2):
        name_index = str(int(i / 2 + 1))
        weight_name = 'W' + name_index
        bias_name = 'b' + name_index
        W = network[weight_name]
        b = network[bias_name]
        a = np.dot(z, W) + b
        if(i != (len(network)//2 - 1) * 2):
            z = sigmoid(a)
        else:
            z = identity_function(a)

    return z


def batch_forward_propagation(x, t, batch_size):
    accuracy_cnt = 0
    if(x.ndim == 1):
        x_batch = x
        print(t)
        y_batch = forward_propagation(network, x_batch)
        p = np.argmax(y_batch, axis=-1)
        print(p)
        accuracy_cnt += np.sum(p == t)
        print("Accuracy : " + str(float(accuracy_cnt)))
    else:
        for i in range(0, len(x), batch_size):
            x_batch = x[i:i+batch_size]
            y_batch = forward_propagation(network, x_batch)
            p = np.argmax(y_batch, axis=-1)
            accuracy_cnt += np.sum(p == t[i:i+batch_size])
        print("Accuracy : " + str(float(accuracy_cnt) / len(x)))
# --------------------------------
# Loss function
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
# --------------------------------


if __name__ == "__main__":
    """
    network = _init_network()
    x = np.array([1.0,0.5])
    y = _forward_propagation(network, x)
    print(y)

    x = np.array([1.0,0.5])
    size = (len(x),3,2,2)
    network = init_network(size)
    y = forward_propagation(network, x)
    print(y)
    print(network)
    """

    # load from pickle
    dataset = load_mnist.load_pickle()

    # for 1 data
    x = dataset['train_img'][0]
    t = dataset['train_label'][0]
    size = (len(x),50,100,10)
    network = init_network(size)
    batch_size = 1
    batch_forward_propagation(x, t, batch_size)

    # batch processing
    x = dataset['train_img']
    t = dataset['train_label']
    batch_size = 100
    batch_forward_propagation(x, t, batch_size)
