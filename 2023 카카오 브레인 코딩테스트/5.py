#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    result = []
    # Write your code here
    for query in queries:
        plusIndex = query - 1
        minusIndex = query - 1
        targetStock = stockData[query - 1]
        while minusIndex >= 0 or plusIndex < len(stockData):
            plusIndex += 1
            minusIndex -= 1
            if minusIndex >= 0 and targetStock > stockData[minusIndex]:
                result.append(minusIndex + 1)
                break
            elif plusIndex < len(stockData) and targetStock > stockData[plusIndex]:
                result.append(plusIndex + 1)
                break
        else:
            result.append(-1)
    
    return result
        
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
