import matplotlib.pyplot as plt
import numpy as np
import sys
from collections import defaultdict
# read in data
author2month = defaultdict(dict)
for line in sys.stdin:
    items = line.strip().split(';')
    author = items[0]
    month = items[1]
    author2month[author][month] = list(items[2].split(','))

def plot_bar_x(labels, x, y):
    indexA = np.arange(len(labels))
    indexB = indexA + 0.4
    plt.bar(indexA, x, color = 'b', width = 0.4)
    plt.bar(indexB, y, color = 'r', width = 0.4)
    plt.xlabel('Month', fontsize=5)
    plt.ylabel('# commits/activities', fontsize=5)
    plt.xticks(indexA + 0.2, labels, fontsize=5, rotation=30)
    plt.title('Plot for frameworks (react, angular) usages per month')
    plt.legend(['React', 'Angular'], loc=2)
    plt.show()

# let's plot the first 10
count = 0
for author, month in author2month.items():
    count += 1
    if count > 10:
        break
    # prepare x and y, i.e., react and angular
    x =[]
    y = []
    labels = []
    sorted_month = sorted(map(int, month.keys()))
    current_month = sorted_month[0]
    while current_month <= sorted_month[-1]:
        if int(str(current_month)[-2:]) > 12:
            current_month -= 12
            current_month += 100
        labels.append(str(current_month))
        if current_month in sorted_month:
            activity = month[str(current_month)]
            x.append(int(activity[0]))
            y.append(int(activity[1]))
        else:
            x.append(0)
            y.append(0)
        current_month += 1
    plot_bar_x(labels, x, y)
