#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
	if n < 0:
		return undefined
	if n == 1:
		return 1
	if n == 0:
		return 1

	return (n * factorial(n-1))

if __name__ == '__main__':
    

    n = int(input())

    result = factorial(n)

    print(result)

"""if (n < 0) return undefined;
    if (n == 0) return 1;

    // Base case
    if (n == 1) return 1;

    // Iterative step
    // (If the function got to this point, it means, that n > 1)
    return n * factorial(n - 1);

    // In order to return the expression on the right side of "return",
    // You need to calculate the `factorial(n - 1)`
    // When you try calculating it, you will see, that now you need to
    //     find out the `factorial(n - 1)` again, but this time the 
    //     `n` is actually `(n - 1)` :)
    // So this way, you are digging into the call stack.
    // At some point you reach the 1. WHICH RETURNS 1. WOOHOO.
    // No need to calculate the `factorial` anymore.
    // Now all the expressions you couldn't evaluate, get evaluated 1 by 1
}"""