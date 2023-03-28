#coding:utf-8
import sys
import json
import random

raw_data_path = './demo_data/raw_data'
output_data_path = './demo_data/SUMMARY.csl'

def split_data():
    all_dataset = []
    with open(raw_data_path+'/train.csv','r',encoding='utf-8') as lines:
        for line in lines:
            data = line.strip().split(',')
            if len(data)<3:continue
            json_data = {'article':data[1],'summarization':data[2]}
            all_dataset.append(json_data)
    random.shuffle(all_dataset)
    train_data = all_dataset[:-2000]
    dev_data = all_dataset[-2000:]
    test_data = dev_data[-1000:]
    dev_data = dev_data[:1000]
    print('train data size :'+str(len(train_data)))
    print('dev data size   :'+str(len(dev_data)))
    print('test data size  :'+str(len(test_data)))
    json.dump(train_data,open(output_data_path+'/train.json','w',encoding='utf-8'),ensure_ascii=False)
    json.dump(dev_data,open(output_data_path+'/dev.json','w',encoding='utf-8'),ensure_ascii=False)
    json.dump(test_data,open(output_data_path+'/test.json','w',encoding='utf-8'),ensure_ascii=False)

#    return train_data,dev_data,test_data
#
# def convert_preliminary_data():


