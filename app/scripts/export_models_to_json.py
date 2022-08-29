# -*- coding: utf-8 -*-
'''
This scripts read the file and each line must to have view like bottom without any empty lines in file:
10.200.3.1 C1921_Beta2 CISCO1921/K9 FCZ1619C48X flash:c1900-universalk9-mz.SPA.157-3.M3.bin
and create uniq list of models. then write output to json 
'''
import json


def generateDict(inFile):
    fileLines = []
    dumpDict = {}
    modelsSet = set()

    #read file
    try:
        with open(inFile, encoding = 'utf-8') as f:
            fileLines = f.readlines()
    except: 
        print("some err with open or read file:", inFile)
        return False

    try:
        for line in fileLines:
            #remove duplictes
            modelsSet.add(line.split()[2])

        for hwModel in modelsSet:
            ipList = []
            for line in fileLines:
                if hwModel == line.split()[2]:
                    ipList.append([line.split()[0], line.split()[1], line.split()[3], line.split()[4]])
                    dumpDict[hwModel] = ipList
    except:
        print("Incorect line ")
        return False
    return dumpDict


#write dump to the file 
def writeOutput(dump, outFile):
    try:
        with open(outFile, 'w') as f:
            json.dump(dump, f)
    except:
        print("can't write:", outFile)
        return False


def main():
    inFile = 'input.txt'
    outFile = 'output.txt'

    if generateDict(inFile):
        #print(generateDict(inFile))
        writeOutput(generateDict(inFile), outFile)


if __name__ == '__main__':
    main()