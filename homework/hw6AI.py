import random
import numpy as np
import io
import pandas as pd

def generator(variable, size, probability):
    return np.random.choice(a=variable, size=size, p=probability)

def frequencyTable(dataset):
    unique, counts = np.unique(dataset, return_counts=True)
    output = []
    for i in range(unique.size):
        line = ''
        line += unique[i] + '\t'
        line += '|\t'
        line += str(counts[i]/dataset.size)
        output.append(line)
    print('\n'.join(output))

def normalizeData(vector):
    alpha = 1/np.sum(vector)
    normalized = vector*alpha
    return normalized

def bayesRule(pB, pAB):
    """
    Calculate
    P(A|B) = P(A,B)/P(B)
    """
    
    return 

if __name__ == '__main__':
    # prob = """Temperature Probability\nhot 0.5\ncold 0.5"""
    # data = io.StringIO(prob)
    # df = pd.read_csv(data, sep=' ')
    # print(df)
    # random_data = generator(["True", "False"], 1000, [0.9, 0.1])
    # frequencyTable(random_data)

    # create joint distribution between Weather and Temperature
    # data = [[0.4, 0.2], [0.1, 0.3]]
    # df = pd.DataFrame(data, index=['sun','rain'],columns=['hot','cold'])
    # print(df)
    # print()

    # # Normalize sun row
    # print(normalizeData(df.iloc[0]))
    # print(df.loc['sun','hot'])

    classes = ['dog', 'cat', 'mouse', 'horse']
    pmf = [0.5, 0.3, 0.1, 0.1]
    a = np.random.choice(a=classes,p=pmf,size=10000)

    unique, counts = np.unique(a, return_counts=True)
    for i in range(len(counts)):
        print(f'{unique[i]}: {counts[i]/a.size}')