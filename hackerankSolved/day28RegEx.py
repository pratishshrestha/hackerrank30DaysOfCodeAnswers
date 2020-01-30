#!/bin/python3

import math
import os
import random
import re
import sys

regexGmail = re.compile("^[a-z\.]+@gmail.com$")

if __name__ == '__main__':
    N = int(input())
    accounts = dict()
    

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if regexGmail.match(emailID):
        	accounts[emailID] = firstName
        

print(*sorted(accounts.values()), sep = '\n')




