"""
referenced from
https://qiita.com/python_walker/items/e4d2ae5b7196cb07402b
"""

import urllib.request
import gzip
import numpy as np
import pickle
import matplotlib.pyplot as plt


def download_mnist(flag=0, dataset_dir='.'):
    url_base = 'http://yann.lecun.com/exdb/mnist/'
    key_file = {
        'train_img':'train-images-idx3-ubyte.gz',
        'train_label':'train-labels-idx1-ubyte.gz',
        'test_img':'t10k-images-idx3-ubyte.gz',
        'test_label':'t10k-labels-idx1-ubyte.gz'
    }

    if(flag == 1):
        for v in key_file.values():
            file_path = dataset_dir + '/' + v
            urllib.request.urlretrieve(url_base + v, file_path)

    return key_file


def load_img_form_gz(file_name, dataset_dir='.'):
    file_path = dataset_dir + '/' + file_name
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, 784)

    return data


def load_label_from_gz(file_name, dataset_dir='.'):
    file_path = dataset_dir + '/' + file_name
    with gzip.open(file_path, 'rb') as f:
        labels = np.frombuffer(f.read(), np.uint8, offset=8)

    return labels


def load_gz(key_file):
    dataset = {}
    dataset['train_img'] = load_img_form_gz(key_file['train_img'])
    dataset['train_label'] = load_label_from_gz(key_file['train_label'])
    dataset['test_img'] = load_img_form_gz(key_file['test_img'])
    dataset['test_label'] = load_label_from_gz(key_file['test_label'])

    return dataset


def save_pickle(dataset, dataset_dir='.'):
    save_file = dataset_dir + '/mnist.pkl'    #拡張子は.pkl
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)    #-1は最も高いプロトコルバージョンで保存する


def load_pickle(dataset_dir='.'):
    save_file = dataset_dir + '/mnist.pkl'    #拡張子は.pkl
    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    return dataset


# one hot encoding for label
def one_hot(label):
    label_num = np.max(label) - np.min(label) + 1
    T = np.zeros((label.size, label_num))
    for i in range(label.size):
        T[i][label[i]] = 1

    return T


# preprocessing normalization
def normalize(key):
    dataset[key] = dataset[key].astype(np.float32)
    dataset[key] /= 255

    return dataset[key]


if __name__ == "__main__":
    # first time
    #key_file = download_mnist()

    # load from download data
    #dataset = load_gz(key_file)

    # save as pickle
    #save_pickle(dataset)

    # load from pickle
    dataset = load_pickle()

    print(dataset['train_img'].shape)
    print(dataset['train_label'].shape)
    """
    example = dataset['train_img'][0].reshape((28, 28))

    plt.imshow(example)
    plt.show()
    """
    print(dataset['train_label'].shape)
    dataset['train_label'] = one_hot(dataset['train_label'])
    print(dataset['train_label'].shape)

    print(np.sum(dataset['train_img'].reshape(-1)))
    dataset['train_img'] = normalize('train_img')
    print(np.sum(dataset['train_img'].reshape(-1)))
