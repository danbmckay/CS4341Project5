class UnaryInclusive:

    def __init__(self, item, bags):
        self.item = item
        self.bags = bags

    def is_final_permissible(self, solution):

        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return True
                else:
                    return False

        return -1


class FittingLimit:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_final_permissible(self, solution):

        is_valid = True
        for a_bag in solution:
            if not self.lower_bound <= len(a_bag) - 1 <= self.upper_bound:
                is_valid = False
                break

        return is_valid


class UnaryExclusive:

    def __init__(self, item, bags):
        self.item = item
        self.bags = bags

    def is_final_permissible(self, solution):

        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return False
                else:
                    return True

        return -1


class BinaryEquals:

    def __init__(self, items):
        self.items = items

    def is_final_permissible(self, solution):

        for a_bag in solution:
            if self.items[0] in a_bag:
                if self.items[1] in a_bag:
                    return True
                else:
                    return False

        return -1


class BinaryNotEquals:

    def __init__(self, items):
        self.items = items

    def is_final_permissible(self, solution):
        for a_bag in solution:
            if self.items[0] in a_bag:
                if self.items[1] in a_bag:
                    return False
                else:
                    return True

        return -1


class MutualInclusive:

    def __init__(self, items, bags):
        self.items = items
        self.bags = bags

    def is_final_permissible(self, solution):

        for a_f_bag in solution:
            for i in range(0, 1):
                if self.items[i] in a_f_bag:
                    if i == 1:
                        opp_i = 0
                    else:
                        opp_i = 1

                    for j in range(0, 1):
                        if self.bags[j] == a_f_bag[0]:
                            if j == 1:
                                opp_j = 0
                            else:
                                opp_j = 1

                                for a_s_bas in solution:
                                    if self.items[opp_i] in a_s_bas:
                                        if self.bags[opp_j] == a_s_bas[0]:
                                            return True
                                        else:
                                            return False

        return True


class WeightLimit:

    def __init__(self, bag, weight):
        self.bag = bag
        self.weight = weight

    def is_permissible(self):
        pass
