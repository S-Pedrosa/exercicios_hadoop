#!/usr/bin/python3

import sys

oldKey = None
TopSale=0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total   
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", TopSale)
        oldKey = thisKey;  # creo que sobra esta liña
        TopSale = 0

    oldKey = thisKey
    if float(thisSale) > TopSale:
        TopSale = float(thisSale)

# Escribe o último par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey, "\t", TopSale)