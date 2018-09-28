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


class Item:

    def __init__(self, item, weight):
        self.item = item
        self.weight = weight


class Bag:

    def __init__(self, letter, capacity):
        self.letter = letter
        self.capacity = capacity


items = []
bags = []
# initialize fitting limit to be able to hold as much as they want
fittingLimit = FittingLimit(0, 26)
unaryInclusives = []
unaryExclusives = []
binaryEquals = []
binaryNotEquals = []
mutualInclusive = []

#parsing through input file and assigning all inital values
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
                items.append(Item(temp[0], temp[1]))
            elif count == 2:
                #bag values
                bags.append(Bag(temp[0], temp[1]))
            elif count == 3:
                #fitting limits
                fittingLimit = FittingLimit(temp[0], temp[1])
            elif count == 4:
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
            elif count == 5:
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
            elif count == 6:
                #binary equals
                binaryEquals.append(BinaryEquals([temp[0], temp[1]]))
            elif count == 7:
                #binary does not equal
                binaryNotEquals.append(BinaryNotEquals([temp[0], temp[1]]))
            elif count == 8:
                #mutual inclusive
                mutualInclusive.append(MutualInclusive([temp[0], temp[1]], [temp[2], temp[3]]))