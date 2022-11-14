import os
import json
import numpy as np
import pandas as pd

def create_length_of_the_file(file1, file2):
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

        perfs = ((perfs1+perfs2)/2).tolist()
        perf = [str(a) for a in perfs]

        di["train_config"] = train1
        d = dict(zip(tgt_langs1, perf))
        di["eval_results"] = d
        l.append(di)
    return l


dir1 = "all_task_ensem/preds/"
dir2 = "all_model_ensem/preds/"

outdir = "ensem/preds/"
for filename in os.listdir(dir1):
    l = {}
    if ".json" in filename:
        print(filename)
        file1 = dir1+filename
        file2 = dir2+filename
        l = create_length_of_the_file(file1, file2)
        print(len(l))

        out = outdir+filename

        with open(out, "w") as outfile:
            json.dump(l, outfile)
