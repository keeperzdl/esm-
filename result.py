#!/usr/bin/python
# coding:utf-8

import os

with open("/home/authenticate/same/toplog", "rb") as data:
    while 1:
        line = data.readline()
        if not line:
            break
        num = int(line.split("|")[1])
        if num > 800:
            print line,

