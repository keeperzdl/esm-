logs_num：原始日志数据  
logs_same_num：命中规则和命中的样本库，文件名是命中规则排序后的hash  
msdn.txt：规则库  
num：计数器，总共跑的样本数量  
pl：命中规则的频率，里边是命中规则排序后的hash，和命中次数的对应关系  
samfunc.py，same.py：主执行程序  
over.py：拿top的执行程序  
same_data.py，result.py：按条件拿top的执行程序，例如拿规则长度超过20的top，over.py不支持over.py里边动态存储了命中规则hash和出现频率没有hash和规则的对应关系。  
white：99%以上为黑的命中规则和规则hash  
