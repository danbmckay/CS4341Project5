import sys

itemWeights = [] * 26
bagSizes = [] * 26
fittingLimits = [] * 2


with open(sys.argv[1], "r") as f:
    count = 0
    for line in f:
        if "#####" in line:
            count += 1
        else:
            temp = line.split()
            #check count value and assign values
            if count == 1:
                #variables
                #use ascii value as index to array
                index = ord(temp[0]) - 65
                itemWeights[index] = temp[1]
            if count == 2:
                #bag values
                # use ascii value as index to array
                index = ord(temp[0]) - 65
                bagSizes[index] = temp[1]
            if count == 3:
                #fitting limits
                fittingLimits[0] = temp[0]
                fittingLimits[1] = temp[1]
            if count == 4:
                #unary inclusive
            if count == 5
                #unary exclusive
            if count == 6:
                #binary equals
            if count == 7:
                #binary does not equal
            if count == 8:
                #mutual inclusive
