#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    while True:
        n = int(input())
        if n < 2 or n > 20:
            continue
        else:
            break
    for i in range(1,11):
    	print(str(n) + ' * ' +'%d' %(i) + ' = ' + str(n*i))
        #print(str(n) + ' * ' + '%d' + ' = ' + str(n*i) %(i) )
