import os
import json
import numpy as np
import pandas as pd


def create_length_of_the_file(dir):
    list = []
    for filename in os.listdir(dir):
        l = {}
        if ".json" in filename:
            f = os.path.join(dir, filename)
            # print(f)
            with open(f,'r') as data_file:
                data = json.loads(data_file.read())

            with open(f,'r') as data_file:
                print(f, len(data_file.readlines()))

            l["file"] = f
            l["length"] = len(data)
            list.append(l)
    return list


def print_dict(file1, file2):
    return []

print("#######################################################")

list1 = create_length_of_the_file("baseline_preds")
print("#######################################################")
list2 = create_length_of_the_file("my_preds")
print("#######################################################")
list3 = create_length_of_the_file("../SumEval/data/test_release")
print("#######################################################")

# with open("my_preds/sumeval_test.json", "r") as f1:
#     data1 = json.loads(f1.read())
#
# with open("baseline_preds/sumeval_test.json", "r") as f2:
#     data2 = json.loads(f2.read())


with open("my_preds/WikiANN_XLMR.json", "r") as f3:
    data3 = json.loads(f3.read())

with open("baseline_preds/WikiANN_XLMR.json", "r") as f4:
    data4 = json.loads(f4.read())

# print(len(data3) , len(data4))
# print(data3[0])
# print(data4[0])

# for i in range(len(data3)):
#     # print(len(data3[i]["train_config"]), len(data4[i]["train_config"]))
#     dict1 = data3[i]["eval_results"]
#     dict2 = data4[i]["eval_results"]
#     list1 = [k for k, v in dict1.items()]
#     list2 = [k for k, v in dict2.items()]
#     print("******************************************")
#     print(list1)
#     print(list2)
#     print("******************************************")


# for i in range(len(data1["examples"])):
#     if data1["examples"][i]["overall_setting"] != data2["examples"][i]["overall_setting"]:
#         print(i, data1["examples"][i]["overall_setting"], data2["examples"][i]["overall_setting"])
#         # print(i)

# for i in range(len(list1)):
#     print(list1[i]["file"], list2[i]["file"])
#     print(list1[i]["length"], list2[i]["length"])
