import re

ipList = []
log_file = open("log.txt", "r")
pattern = re.compile(r'Failed password')
ipAddRegex = re.compile(r'\b[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
for lines in log_file.readlines():
    findIP = ipAddRegex.search(lines)
    findFormula = pattern.search(lines)
    if findIP and findFormula:
        ipList.append(findIP.group())

