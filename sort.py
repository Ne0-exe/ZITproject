import ipList from analyse as ipL

if __name__ == "__main__":

    sortDict = {}
    def sortAlg(ipL):
        for i in range(len(ipL)):
            if len(sortDict) == 0:
                continue
            for a, b in sortDict.items():
                if ipL[i] == a:
                    b = b + 1
                else:
                    sortDict[ipL[i]] = 1

        print(sortDict)




