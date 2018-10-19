#!/usr/bin/python
# coding:utf-8

import json
import sys
import esm
import os
from kafka import KafkaConsumer
import requests
import time
import datetime
import hashlib

def LoadDB(fname):
    fp = open(fname, "rt")
    data = fp.readlines()
    data = ''.join(data).strip('\n').splitlines()
    fp.close()
    return data

# create database
dict_db = {}
seach_db = esm.Index()
my_db = LoadDB("./msdn.txt")

i = 0
for key in my_db:
    if len(key) < 5:
        continue
    seach_db.enter(key)
    dict_db[key] = i
    i = i + 1

seach_db.fix()

def ScanMemory(fname, data):
     sign_bit = [0] * 160000
     sign_item = []
     detect_list = seach_db.query(data)
     for item in detect_list:
         idx = dict_db[item[1]]
         if sign_bit[idx] != 1:
             sign_item.append(item[1])
         sign_bit[idx] = 1
     return fname, sign_bit, sign_item

def kafka_run():
    consumer = KafkaConsumer('PREPROCESS_RESULT_QUEUE',group_id='group_samfunc_2',bootstrap_servers=['10.255.65.3:9092'],)
    n=0
    dict_data={}
    for message in consumer:
        try:
            data = json.loads(message.value)
            url = data[u'data'][u'download_url']
            file_name = url.split('/')[-1]
            r = requests.get(url)
        except Exception, e:
            continue
        if r.status_code != 200:
            continue

        with open("/home/authenticate/same/num", "wb") as test:
            print >> test,n
        n+=1
        data=r.content
        fname, sign_bit, sign_item = ScanMemory(file_name, data)

        today = datetime.date.today()
        now_time = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d_%H_%M')
        sign_item.sort()
        signature = hashlib.md5(str(sign_item)).hexdigest()
        if sign_item != []:
            if not os.path.exists("/home/authenticate/same/logs_num/%s" % today):
                os.mkdir("/home/authenticate/same/logs_num/%s" % today)
            with open("/home/authenticate/same/logs_num/%s/log%s" % (today,time1_str), "ab") as data:
                print >> data, file_name,signature,sign_item
            with open("/home/authenticate/same/logs_same_num/%s" %signature , "ab+") as data:
                data_all = data.read()
                if file_name not in data_all:
                    print >> data, file_name
            if signature not in dict_data:
                dict_data[signature]=1
            else:
                dict_data[signature]+=1
            if n%100 == 0:
                with open("/home/authenticate/same/pl", "wb") as data:
                    print >> data, dict_data

if __name__ == '__main__':
    kafka_run()

