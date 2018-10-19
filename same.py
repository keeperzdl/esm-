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
    with open(path, "rb") as data:
        dict_data = {}
        while 1:
            line = data.readline()
            if not line:
                break
            signature = line[33:65]
            list_same = line[66:]
            dict_data[signature]=list_same
    list_signature = dict_data.keys()
    for ele_signature in list_signature:
        with open("/home/authenticate/same/logs_same_num/%s" % ele_signature, "r+") as data:
            old = data.read()
            if dict_data[ele_signature] in old:
                continue
            else:
                print ele_signature
                data.seek(0)
                print >> data, dict_data[ele_signature]
                print >> data, old

if __name__ == '__main__':
    while 1:
        handle = getRules("/home/authenticate/same/logs_num/")
        for ele in handle:
            read(ele)
    # read("/home/authenticate/same/logs/2018-06-12/log2018-06-12_00_11")