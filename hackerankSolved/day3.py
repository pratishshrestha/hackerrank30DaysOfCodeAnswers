#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print('Input the value of N:    ')
    while True:
        N = int(input())
        if N < 1 or N > 100:
            print('Enter between 1 to 100')
            continue
        else:
            break
    if (N % 2) != 0:
        print('Weird')
    elif (N % 2) ==0:
        if N in range(2,6):
            print('Not Wierd')
        elif N in range(6,21):
            print('Weird')
        elif N > 20:
            print('Not Weird')