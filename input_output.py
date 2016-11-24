# -*- coding: utf-8 -*-

import random
import sys

def read_file(filename):
    f = open(filename,'r')
    
    data = []
    for line in f:
        line = line.strip('\n').split(",")
        line[1:4] = [ float(x) for x in line[1:4] ]
        data.append(line)
    f.close()
    return data

def write_file(data, filename):
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([repr(x) for x in item]))
        f.write('\n')
    f.close()