import sys

class UnaryInclusive:

    def __init__(self, item, bags):
        self.item = item
        self.bags = bags

    def is_permissible(self, solution):

        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return True
                else:
                    return False

        return True


class FittingLimit:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_permissible(self, solution):

        # for a_bag in solution:
        #     if  len(solution) < self.lower_bound +1 :
        pass



class UnaryExclusive:

    def __init__(self, item, bags):
        self.item = item
        self.bags = bags

    def is_permissible(self):
        pass


class BinaryEquals:

    def __init__(self, items):
        self.items = items

    def is_permissible(self):
        pass


class BinaryNotEquals:

    def __init__(self, items):
        self.items = items

    def is_permissible(self):
        pass


class MutualInclusive:

    def __init__(self, items, bags):
        self.items = items
        self.bags = bags

    def is_permissible(self):
        pass


itemWeights = [0] * 26
bagSizes = [0] * 26
#initialize fitting limit to be able to hold as much as they want
fittingLimit = FittingLimit(0, 26)
unaryInclusives = []
unaryExclusives = []
binaryEquals = []
binaryNotEquals = []
mutualInclusive = []


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
                index = ord(temp[0]) - 97
                bagSizes[index] = temp[1]
            if count == 3:
                #fitting limits
                fittingLimit = FittingLimit(temp[0], temp[1])
            if count == 4:
                #unary inclusive
                tempItems = []
                first = True
                for t in temp:
                    if first:
                        bag = t
                        first = False
                    else:
                        tempItems.append(t)
                unaryInclusives.append(UnaryInclusive(bag, tempItems))
            if count == 5:
                #unary exclusive
                tempItems = []
                first = True
                for t in temp:
                    if first:
                        bag = t
                        first = False
                    else:
                        tempItems.append(t)
                unaryExclusives.append(UnaryExclusive(bag, tempItems))
            if count == 6:
                #binary equals
                binaryEquals.append(BinaryEquals([temp[0], temp[1]]))
            if count == 7:
                #binary does not equal
                binaryNotEquals.append(BinaryNotEquals([temp[0], temp[1]]))
            if count == 8:
                #mutual inclusive
                mutualInclusive.append(MutualInclusive([temp[0], temp[1]], [temp[2], temp[3]]))