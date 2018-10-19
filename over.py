#!/usr/bin/python
# coding:utf-8

import json
import operator
import shutil
dict_data={}
with open("/home/authenticate/same/pl", "r") as data:
    dict_data_2 = eval(data.read())
for ele in dict_data_1:
    if ele not in dict_data:
        dict_data[ele] = dict_data_1[ele]
    else:
        dict_data[ele] = dict_data[ele] + dict_data_1[ele]
for ele in dict_data_2:
    if ele not in dict_data:
        dict_data[ele] = dict_data_2[ele]
    else:
        dict_data[ele] = dict_data[ele] + dict_data_2[ele]

top = sorted(dict_data.items(), key=operator.itemgetter(1))[-1000:]
for tup in top:
    print tup
    file_name = tup[0]
    start_path = "/home/authenticate/same/logs_same_num/%s"%file_name
    count = len(open(start_path, 'rU').readlines())
    if count>100:
        end_path = "/home/authenticate/same/top/%s"%file_name
        shutil.copyfile(start_path,end_path)

