import analyse
import sys

ipL = analyse.ipList
sortDict = {ipL[0]:1}
sortDict = {i:ipL.count(i) for i in ipL}

with open('ips.txt', 'w') as sys.stdout:
    print(sortDict)



