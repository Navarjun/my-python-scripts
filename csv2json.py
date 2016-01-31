#
# Created by Navarjun
# 31 Jan 2016
#
# This simple scripts converts any csv file into json file
# just copy this script in the same directory as your csv file
# and run the following command:
#   python csv2json.py filename.csv

from sys import argv

script, filename = argv

iterator = 0
fieldNames = []

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

target = open(filename.replace('.csv', '.json'),'w')
target.truncate()
target.write('[\n')
with open(filename) as f:
    firstValueIteration = True
    for line in f:
        line = line.replace('\n', '')
        if (iterator == 0):
            fieldNames = line.split(',')
            hasGotFieldNames = True
        else:
            fieldValues = line.split('","')
            if len(fieldValues) != len(fieldNames):
                iterator+=1
                continue
            if firstValueIteration:
                target.write('\t{\n')
                firstValueIteration = False
            else:
                target.write(',\n\t{\n')
            for i in range(0, len(fieldNames)):
                fieldValue = fieldValues[i]
                fieldValue = fieldValue.replace('"','')
                if isNumber(fieldValue) == False:
                    fieldValue = '"'+fieldValue+'"'
                target.write('\t\t"'+fieldNames[i]+'":'+fieldValue)
                if len(fieldNames) - 1 != i:
                    target.write(',')
                target.write('\n')
            target.write('\t}')
        iterator+=1
target.write('\n]\n')
target.close()