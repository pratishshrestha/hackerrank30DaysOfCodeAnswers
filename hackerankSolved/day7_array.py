
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
   # for i in range(0, n):
	#    elements = int(input())
    #arr.append(elements)
    #print(str(elements) + " added to A")
    arr = list(reversed(arr))
    print(' '.join(map(str,arr)))

"""input() looks like it gets the next line of input. From the example this is the string "1 2 3 4 5\n" (it has a newline on the end).

rstrip() then removes whitespace at the right end of the input, including the newline.

split() with no arguments splits on whitespace, transforming the input to an iterable of strings. e.g. ['1', '2', '3', '4', '5']

map(int, sequence) applies int to each string. e.g. int('1') -> 1, int('2') -> 2 etc.. So your sequence of strings is now a sequence of integers.

Finally list(seq) transforms the sequence to a list type. So now you have [1,2,3,4,5]."""