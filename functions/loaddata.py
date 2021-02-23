import csv
import numpy as np
import os


def loaddata():
    cwd = os.getcwd()

    #Load big currents from CSV
    read_big = csv.reader(open(cwd+'/functions/data/currents_big.csv', 'rt'), delimiter=',')
    currents_big = list(read_big)
    currents_big = np.array(currents_big)

    #Load location of big currents from CSV
    read_XYZbig = csv.reader(open(cwd+'/functions/data/XYZ_big.csv', 'rt'), delimiter=',')
    XYZ_big = list(read_XYZbig)
    XYZ_big = np.array(XYZ_big)

    #Load small currents from CSV
    read_small = csv.reader(open(cwd+'/functions/data/currents_small.csv', 'rt'), delimiter=',')
    currents_small = list(read_small)
    currents_small = np.array(currents_small)

    #Load location of small currents from CSV
    read_XYZsmall = csv.reader(open(cwd+'/functions/data/XYZ_small.csv', 'rt'), delimiter=',')
    XYZ_small = list(read_XYZsmall)
    XYZ_small = np.array(XYZ_small)
    return currents_big, XYZ_big, currents_small, XYZ_small