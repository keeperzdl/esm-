#!/usr/bin/python
# coding:utf-8
import hashlib
import os

def getRules(path_name):
    filepath = []
    g = os.walk(path_name)
    for path, d, filelist in g:
        for filename in filelist:
            rupath = os.path.join(path, filename)
            filepath.append(rupath)
    return filepath

def read(path):
    with open(path, "r") as data:
        try:
            data_all = data.read()
            data_list = eval(data_all.split("]")[0]+"]")
            if len(data_list)>20:
                data_hash = data_all.split("]")[1].replace(' ','').replace('\n','')
                hash_signature = path.split("/")[-1]
                len_data = len(data_hash)/32
                string = hash_signature+"|"+str(len_data)
                print string
        except:
            pass

if __name__ == '__main__':
    handle = getRules("/home/authenticate/same/logs_same_num/")
    for ele in handle:
        read(ele)
    # read("/home/authenticate/same/logs_same/7c4712d9582ced7976aea552ad885d4a")

#python same_data.pt >> pl