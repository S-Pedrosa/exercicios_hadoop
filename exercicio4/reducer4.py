#!/usr/bin/python3

import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", salesMax)
        # oldKey = thisKey;
        salesMax = 0

    oldKey = thisKey
    if (thisSale >= salesMax):
        salesMax = float(thisSale)

if oldKey != None:
    print(oldKey, "\t", salesMax)