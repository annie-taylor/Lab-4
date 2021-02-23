import random
import numpy as np

def randplacement(XYZ_big):
    # Find 10 random positions in 100um cube for hillock origin
    neurons = []
    for i in range(10):
        randx = random.random() * 100
        randy = random.random() * 100
        randz = random.random() * 100
        neurons.append([randx, randy, randz])

    XYZ1 = [[neurons[0][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[0][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[0][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ2 = [[neurons[1][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[1][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[1][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ3 = [[neurons[2][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[2][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[2][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ4 = [[neurons[3][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[3][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[3][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ5 = [[neurons[4][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[4][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[4][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ6 = [[neurons[5][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[5][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[5][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ7 = [[neurons[6][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[6][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[6][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ8 = [[neurons[7][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[7][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[7][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ9 = [[neurons[8][0] + float(x) for x in XYZ_big[:, 0]],
            [neurons[8][1] + float(y) for y in XYZ_big[:, 1]],
            [neurons[8][2] + float(z) for z in XYZ_big[:, 2]]]
    XYZ10 = [[neurons[9][0] + float(x) for x in XYZ_big[:, 0]],
             [neurons[9][1] + float(y) for y in XYZ_big[:, 1]],
             [neurons[9][2] + float(z) for z in XYZ_big[:, 2]]]
    return np.transpose(XYZ1),np.transpose(XYZ2),np.transpose(XYZ3),np.transpose(XYZ4),np.transpose(XYZ5), np.transpose(XYZ6), np.transpose(XYZ7), np.transpose(XYZ8), np.transpose(XYZ9), np.transpose(XYZ10)