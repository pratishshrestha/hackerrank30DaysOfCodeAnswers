#!/bin/python3

import math
import os
import random
import re
import sys

def decTobin(n):
    if n == 0:
        return ""
    else:
    	return decTobin(n//2) + str(n%2)
    	

if __name__ == '__main__':
    n = int(input())
    result = list(map(int, decTobin(n)))
    #print(result)
    count, highest_count = 0, 0

    for i in range(0, len(result)):
    	if result[i] == 1:
    		count += 1
    	elif result[i] == 0:
    		if highest_count < count:
    			highest_count = count
    			count = 0
    print(highest_count)



    




