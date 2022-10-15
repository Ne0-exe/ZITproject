import re

ip_list = []
log_file = open("log.txt", "r")
pattern = "Failed password"
for lines in log_file.readlines():
	 if re.search(pattern, lines):
	 	ip_list.append(re.search(r'\b[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', lines))

print(ip_list)