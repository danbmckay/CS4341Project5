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
