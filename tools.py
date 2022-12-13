# Import libraries
import matplotlib.pyplot as plt
import csv
from math import log
from math import exp
from math import ceil

def loadData(filename):
    """
    Charge les données d'un fichier CSV
    """
    with open(filename, newline='', encoding='UTF-8') as csvfile:
        tons = {}
        data = csv.reader(csvfile, delimiter=',', quotechar='#')
        header = next(data)
        sources = next(data)
        for row in data:
            tons[int(row[0])] = int(row[1])

        X = list(tons.keys())
        Y = list(tons.values())

        return X, Y