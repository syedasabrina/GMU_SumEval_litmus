import os
import json
import numpy as np
import pandas as pd
import math


def plot_graph(x, y, file, title, xlabel, ylabel, c):
    from matplotlib import pyplot as plt
    plt.figure(figsize = (10, 5))
    bars = plt.bar(x, y, width=0.6)
    for bar in bars:
        yval = bar.get_height()
        yval = "{:.3f}".format(yval)
        plt.text(bar.get_x(), float(yval)+0.001, yval)
    # plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.tick_params(axis='x', labelsize=16)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig(file)



with open("error_per_task.json",'r') as data_file:
    data = json.loads(data_file.read())

size = len(data)
# print(size)
task = []
model = []
rmse = []

for i in range(size):
    filename = data[i]['filename'].split("_")
    task.append(filename[0])
    model.append(filename[1])
    rmse.append(data[i]['rmse'])

avg_task = ['XNLI', 'WikiANN', 'UDPOS']
avg_rmse = [(rmse[0]+rmse[1]+rmse[4]+rmse[5])/4, (rmse[2]+rmse[7])/2, (rmse[3]+rmse[6])/2]


x = avg_task
y = avg_rmse
file = "graphs/error_per_task.png"
title = "MAE for each task for Surprise Test Set"
xlabel = "Task"
ylabel = "Mean Absolute Error"
color = ['green', 'red', 'blue']
plot_graph(x, y, file, title, xlabel, ylabel, color)

x = []
y = []
with open("error_per_lang.json",'r') as data_file:
    data = json.loads(data_file.read())

size = len(data)
task = []
model = []
rmse = []
# print(size)
l = []
for i in range(size):
    filename = data[i]['file']
    file = filename.split("_")
    task = filename[0]
    model = filename[1]
    d = data[i]['error_lang']
    tgt_langs = list(d.keys())
    err = np.array(list(d.values()), dtype = float)

    print(filename)
    print(tgt_langs)
    print(err)

    x = tgt_langs
    y = err
    file = "graphs/error_per_lang/"+filename+".png"
    title = "MAE for each Language for Surprise Test Set"
    xlabel = "Target Languages"
    ylabel = "Mean Absolute Error"
    color = ['green', 'red', 'blue', 'yellow', 'indigo', 'orange', 'cyan']
    plot_graph(x, y, file, title, xlabel, ylabel, color)
