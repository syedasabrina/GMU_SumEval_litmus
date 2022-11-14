import os
import json
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error as mae

# 1 is me
def create_errors_of_data(file1, file2):
    with open(file1,'r') as data_file:
        data1 = json.loads(data_file.read())
    with open(file2,'r') as data_file:
        data2 = json.loads(data_file.read())

    size = len(data1)
    # print(size)
    l = []
    for i in range(size):
        di = {}
        train1 = data1[i]['train_config']
        train2 = data2[i]['train_config']

        d = data1[i]['eval_results']
        tgt_langs1 = list(d.keys())
        perfs1 = np.array(list(d.values()), dtype = float)

        d = data2[i]['eval_results']
        tgt_langs2 = list(d.keys())
        perfs2 = np.array(list(d.values()), dtype = float)
        error = np.absolute(perfs1-perfs2)

        di["train_config"] = train1
        d = dict(zip(tgt_langs1, error))
        di["eval_error"] = d
        l.append(di)
    return l

def create_rmse_per_task(file1, file2):
    with open(file1,'r') as data_file:
        data1 = json.loads(data_file.read())
    with open(file2,'r') as data_file:
        data2 = json.loads(data_file.read())

    size = len(data1)
    # print(size)
    l = []
    for i in range(size):
        di = {}
        train1 = data1[i]['train_config']
        train2 = data2[i]['train_config']

        d = data1[i]['eval_results']
        tgt_langs1 = list(d.keys())
        y_pred = np.array(list(d.values()), dtype = float)

        d = data2[i]['eval_results']
        tgt_langs2 = list(d.keys())
        y_test = np.array(list(d.values()), dtype = float)

        # mse = np.square(np.subtract(y_test,y_pred)).mean()
        # rmse = math.sqrt(mse)

        rmse = mae(y_test, y_pred)

        l.append(rmse)
    return np.average(np.array(l))


def create_average_perf_per_lang(file):
    with open(file,'r') as data_file:
        data = json.loads(data_file.read())
    l = []
    size = len(data)

    # p = np.zeros()
    # print(size)
    d = data[0]['eval_error']
    tgt_langs = list(d.keys())
    error = np.array(list(d.values()), dtype = float)
    flag = 0

    for i in range(size):
        di = {}
        train = data[i]['train_config']

        d = data[i]['eval_error']
        tgt_langs1 = list(d.keys())
        if tgt_langs1 != tgt_langs :
            flag = -1
            break
        error1 = np.array(list(d.values()), dtype = float)

        error = (error+error1)

    error = error/size

    if flag == -1:
        print("NOT ALL SAME EVAL LANG")

    return tgt_langs, error


dir1 = "ensem/preds/"
dir2 = "test_gold/"

outdir = "analysis/preds/"
error_per_task = []
for filename in os.listdir(dir1):
    l = {}
    t = {}
    if ".json" in filename:
        file1 = dir1+filename
        file2 = dir2+filename
        l = create_errors_of_data(file1, file2)

        if "surprise" in filename:
            t["filename"] = filename
            t["rmse"] = create_rmse_per_task(file1, file2)
            error_per_task.append(t)

            out = outdir+filename
            with open(out, "w") as outfile:
                json.dump(l, outfile)
        # p = create_average_perf_per_lang(file1)
        # break

out = "analysis/error_per_task.json"
with open(out, "w") as outfile:
    json.dump(error_per_task, outfile)


dir = "analysis/preds/"

error_per_lang = []
for filename in os.listdir(dir):
    l = {}
    if ".json" in filename:
        file = dir+filename
        l["file"] = filename
        lang, err = create_average_perf_per_lang(file)
        d = dict(zip(lang, err))
        l["error_lang"] = d
        error_per_lang.append(l)

out = "analysis/error_per_lang.json"
with open(out, "w") as outfile:
    json.dump(error_per_lang, outfile)

        # p = create_average_perf_per_lang(file1)
        # break
