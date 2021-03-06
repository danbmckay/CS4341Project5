import sys
import collections
import time


class UnaryInclusive:

    def __init__(self, item, bags):
        self.item = item
        self.bags = bags

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return True
                else:
                    return False

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
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

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if not len(a_bag) - 1 <= self.upper_bound:
                return False

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
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

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return False
                else:
                    return True

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.item in a_bag:
                if a_bag[0] in self.bags:
                    return False
                else:
                    return True

        return -1


class BinaryEqual:

    def __init__(self, items):
        self.items = items

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.items[0] in a_bag:
                if self.items[1] in a_bag:
                    return True
                else:
                    for s_bag in solution:
                        if self.items[1] in s_bag:
                            return False
            if self.items[1] in a_bag:
                if self.items[0] in a_bag:
                    return True
                else:
                    for s_bag in solution:
                        if self.items[0] in s_bag:
                            return False

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.items[0] in a_bag:
                if self.items[1] in a_bag:
                    return True
                else:
                    return False

        return -1


class BinaryNotEqual:

    def __init__(self, items):
        self.items = items

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_bag in solution:
            if self.items[0] in a_bag:
                if self.items[1] in a_bag:
                    return False
                else:
                    for s_bag in solution:
                        if self.items[1] in s_bag:
                            return True
            if self.items[1] in a_bag:
                if self.items[0] in a_bag:
                    return False
                else:
                    for s_bag in solution:
                        if self.items[0] in s_bag:
                            return True

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
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

    def is_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for f_bag in solution:
            opp_i = 0
            opp_j = 0
            for i in range(0, 2):
                if self.items[i] in f_bag:
                    if i == 1:
                        opp_i = 0
                    else:
                        opp_i = 1

                    for j in range(0, 2):
                        if self.bags[j] in f_bag:
                            if j == 1:
                                opp_j = 0
                            else:
                                opp_j = 1

                            for a_s_bas in solution:
                                if self.items[opp_i] in a_s_bas:
                                    if self.bags[opp_j] in a_s_bas:
                                        return True
                                    else:
                                        return False

                            return True

        return True

    def is_final_permissible(self, solution):
        global consistancy_checks
        consistancy_checks += 1
        for a_f_bag in solution:
            for i in range(0, 1):
                if self.items[i] in a_f_bag:
                    if i == 1:
                        opp_i = 0
                    else:
                        opp_i = 1

                    for j in range(0, 1):
                        if self.bags[j] in a_f_bag:
                            if j == 1:
                                opp_j = 0
                            else:
                                opp_j = 1

                            for a_s_bas in solution:
                                if self.items[opp_i] in a_s_bas:
                                    if self.bags[opp_j] in a_s_bas:
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


class Item:

    def __init__(self, item, weight):
        self.letter = item
        self.weight = weight
        self.selected = False
        self.num_constraints = 0

    # return the possible bags this item can go into
    def possible_values(self, constraints, bags):
        values = []
        pass_count = 0
        for a_bag in bags:
            a_bag.items.append(self)
            self.selected = True
            temp_solution = make_solutions(bags)
            if not a_bag.is_permissible():
                pass
            else:
                pass_count = 0
                for a_constraint in constraints:
                    if a_constraint == []:
                        pass_count += 1
                    for const in a_constraint:
                        if not const.is_permissible(temp_solution):
                            break
                        pass_count += 1
            a_bag.remove_item(self)
            self.selected = False
            if pass_count == 5:
                # this means that there are no constraints
                values.append(a_bag.letter)
        return values


class Bag:

    def __init__(self, letter, capacity):
        self.letter = letter
        self.capacity = capacity
        self.items = []

    def is_permissible(self):
        global consistancy_checks
        consistancy_checks += 1
        check_weight = 0
        for an_item in self.items:
            check_weight += an_item.weight

        if check_weight <= self.capacity:
            return True
        else:
            return False

    def is_final_permissible(self):
        global consistancy_checks
        consistancy_checks += 1
        check_weight = 0
        for an_item in self.items:
            check_weight += an_item.weight

        if (int((self.capacity) * .9)) <= check_weight <= self.capacity:
            return True
        else:
            return False

    def remove_item(self, an_item):
        if an_item in self.items:
            self.items.remove(an_item)


def make_solutions(the_bags):
    my_bags = []
    for a_bag in the_bags:
        temp_list = [a_bag.letter]
        for an_item in a_bag.items:
            temp_list.append(an_item.letter)
        my_bags.append(temp_list)

    return my_bags


# adds an item to a bag returns if it was successful or there was no way to add an item
# checks for failed states
def select_unassigned(fails, constraints, things, a_heuristic):
    # minimum remaining value heuristic
    if a_heuristic == "MRV":
        counter = 0
        # select the most constrained item
        amount_constrained = []
        for an_item in things[1]:
            amount_constrained.append(0)
            if not an_item.selected:
                for a_bag in things[0]:
                    a_bag.items.append(an_item)
                    temp_solution = make_solutions(things[0])
                    if not a_bag.is_permissible():
                        amount_constrained[counter] += 1
                    else:
                        for a_constraint_type in constraints:
                            for a_constraint in a_constraint_type:
                                if not a_constraint.is_permissible(temp_solution):
                                    amount_constrained[counter] += 1
                                    break
                    a_bag.remove_item(an_item)
            else:
                amount_constrained[counter] = -1
            counter += 1

        max_constraints = max(amount_constrained)

        # check if the item is totally constrained (can't be placed in any bag)
        # this would mean the item can never be placed so just stop trying
        # if max_constraints == len(things[0]):
        #     return False

        selected_item = things[1][amount_constrained.index(max_constraints)]

        # this is the degree heuristic for a tie break between choices
        for i in range(0, len(amount_constrained)):
            temp_highest_degree = 0
            if amount_constrained[i] == max_constraints:
                if things[1][i].num_constraints > temp_highest_degree:
                    selected_item = things[1][i]
                    temp_highest_degree = things[1][i].num_constraints

        # put it in the first bag that it can go into
        for a_bag in things[0]:
            is_placed = True
            a_bag.items.append(selected_item)
            temp_solution = make_solutions(things[0])
            if not a_bag.is_permissible():
                a_bag.remove_item(selected_item)
                is_placed = False
            else:
                for a_constraint_type in constraints:
                    for a_constraint in a_constraint_type:
                        if not a_constraint.is_permissible(temp_solution):
                            a_bag.remove_item(selected_item)
                            is_placed = False
                            break
            if check_been_here(fails, temp_solution):
                a_bag.remove_item(selected_item)
                is_placed = False

            if is_placed:
                selected_item.selected = True
                return [a_bag, selected_item]

        return False

    # using a Least constraing value choose the the correct item
    # pick first item that is unassigned
    elif a_heuristic == "LCV":
        for an_item in things[1]:
            if not an_item.selected:
                # put the first item not selected in a bag
                return LCV(an_item, things[1], things[0], constraints)

    elif a_heuristic == "none":
        selected_item = False
        for an_item in things[1]:
            if not an_item.selected:
                selected_item = an_item

        for a_bag in things[0]:
            is_placed = True
            a_bag.items.append(selected_item)
            temp_solution = make_solutions(things[0])
            if not a_bag.is_permissible():
                a_bag.remove_item(selected_item)
                is_placed = False
            else:
                for a_constraint_type in constraints:
                    for a_constraint in a_constraint_type:
                        if not a_constraint.is_permissible(temp_solution):
                            a_bag.remove_item(selected_item)
                            is_placed = False
                            break
            if check_been_here(fails, temp_solution):
                a_bag.remove_item(selected_item)
                is_placed = False

            if is_placed:
                selected_item.selected = True
                return [a_bag, selected_item]

        return False
    return False


# Least constraining value heuristic function
# item: The item to be added to a bag
# all_items: all of the items in the problem
# bags: all of the bags in the problem
# constraints: all of the constraints
def LCV(item, all_items, bags, constraints):
    # maximum number of remaining values and index of where it occurred, setting placeholders for now
    max_rem_vals, max_index, temp_rem_vals = 0, 'b', 0
    # try putting item in all bags, see which bag rules out fewest choices for others
    for a_bag in bags:
        a_bag.items.append(item)
        item.selected = True
        constraint_satisfied = True
        temp_solution = make_solutions(bags)
        # check to make sure this doesnt violate any constraints
        for a_constraint_type in constraints:
            for a_constraint in a_constraint_type:
                if not a_constraint.is_permissible(temp_solution):
                    constraint_satisfied = False

        if a_bag.is_permissible() and constraint_satisfied:
            # check remaining values on other items
            for i in all_items:
                if not i.selected:
                    remaining_vals = len(i.possible_values(constraints, bags))
                    if remaining_vals != 0:
                        temp_rem_vals += remaining_vals
                    else:
                        # don't want a solution with something with no vals left
                        break
                elif i.letter == item.letter:
                    # this is needed
                    temp_rem_vals += 1
            if temp_rem_vals > max_rem_vals:
                # overwrite the old max remaining values
                max_rem_vals = temp_rem_vals
                max_index = a_bag.letter
        a_bag.remove_item(item)
        item.selected = False
    # time to put item in bag
    for a_bag in bags:
        if a_bag.letter == max_index:
            a_bag.items.append(item)
            item.selected = True
            return [a_bag, item]
    return False

# check if this solution has already occurred True if the board state happened
def check_been_here(solutions, a_solution):
    found_dup = False
    for temp_solution in solutions:
        found_diff = False
        for a_bag in range(0, len(temp_solution)):
            if not collections.Counter(temp_solution[a_bag]) == collections.Counter(a_solution[a_bag]):
                found_diff = True
        if not found_diff:
            found_dup = True

    return found_dup


# does the back tracking with a possible specific heuristic
# fails: solution sets that have failed
# constraints: List of constraints
# things: The list of bags and items in them
# a_heuristic: whichever heuristic we are solving (min remaining value, least constrained value, etc.)
def backtrack(fails, constraints, things, a_heuristic, a_file):
    # check if the assignment is complete
    # make the assignment from what we have in the bags currently
    assignment = make_solutions(things[0])
    satisfied = True
    # check constraints
    for a_constraint_type in constraints:
        for a_constraint in a_constraint_type:
            if not a_constraint.is_final_permissible(assignment):
                satisfied = False
                break

    # check the bag weights
    for a_bag in things[0]:
        if not a_bag.is_final_permissible():
            satisfied = False
            break

    all_items = True
    num_not_selected = 0
    # check that all items are assigned to a bag
    for an_item in things[1]:
        if not an_item.selected:
            num_not_selected += 1
            all_items = False
            satisfied = False

    if all_items and not satisfied:
        return False
    if satisfied:
        return assignment

    is_assignment = False

    for i in range(0, num_not_selected):
        # select an unassigned item

        is_assignment = select_unassigned(fails, constraints, things, a_heuristic)

        if is_assignment:
            temp_solution = make_solutions(things[0])
            write_to_file = "the bag choosen is bag: " + str(
                is_assignment[0].letter) + ", and the item is item: " + str(
                is_assignment[1].letter) + "\n" + "so this is the current answer state: \n"
            for a_bag in temp_solution:
                write_to_file += "bag " + str(a_bag[0]) + " contains items: "
                for j in range(1, len(a_bag)):
                    write_to_file += str(a_bag[j]) + ", "
                write_to_file += "\n"
            write_to_file += "\n"
            a_file.write(write_to_file)
            # go deeper
            temp_result = backtrack(fails, constraints, things, a_heuristic, a_file)
            # if there is a result return it, if theres not get another assignment with the failed states in there now
            if temp_result:
                return temp_result
            else:
                is_assignment[0].remove_item(is_assignment[1])
                is_assignment[1].selected = False
        # no more possible assignments
        else:
            fails.append(make_solutions(things[0]))

            return False

    fails.append(make_solutions(things[0]))
    return False


# Performs the backtracking search
# uis, uexs: unary inclusive/exclusive constraints
# bes, bnes: binary inclusive/exclusive constraints
# mis: mutual inclusive constraints
# bags: list of bags/capacity
# items: list of items/weights
# a_heuristic: the heuristic to perform with
def backtracking_search(uis, uexs, bes, bnes, mis, bags, items, a_heuristic, a_file):
    constraints = [uis, uexs, bes, bnes, mis]
    things = [bags, items]
    return backtrack([], constraints, things, a_heuristic, a_file)


def reset(bags, items):
    for a_bag in bags:
        a_bag.items = []

    for an_item in items:
        an_item.selected = False

def print_results(bags):
    for a_bag in bags:
        first_line = str(a_bag.letter) + " "
        sum_of_items = 0
        for an_item in a_bag.items:
            sum_of_items += an_item.weight
            first_line += str(an_item.letter) + " "
        print(first_line)
        second_line = "number of items: " + str(len(a_bag.items))
        print(second_line)
        third_line = "total weight: " + str(sum_of_items) + "/" + str(a_bag.capacity)
        print(third_line)
        fourth_line = "wasted capacity: " + str(a_bag.capacity - sum_of_items)
        print(fourth_line)
        print()


# global consistancy_checks
consistancy_checks = 0
items = []
items_letter = []
bags = []
bags_letter = []
# initialize fitting limit to be able to hold as much as they want
fittingLimit = FittingLimit(0, 26)
unary_inclusives = []
unary_exclusives = []
binary_equals = []
binary_not_equals = []
mutual_inclusives = []

# parsing through input file and assigning all inital values
with open(sys.argv[1], "r") as f:
    count = 0
    for line in f:
        if "#####" in line:
            count += 1
        else:
            temp_line = line.split()
            # check count value and assign values
            if count == 1:
                # variables
                items.append(Item(temp_line[0], int(temp_line[1])))
                items_letter.append(temp_line[0])
            elif count == 2:
                # bag values
                bags.append(Bag(temp_line[0], int(temp_line[1])))
                bags_letter.append(temp_line[0])
            elif count == 3:
                # fitting limits
                fittingLimit = FittingLimit(temp_line[0], temp_line[1])
            elif count == 4:
                # unary inclusive
                temp_bags = []
                item = 'a'
                first = True
                for a_letter in temp_line:
                    if first:
                        item = a_letter
                        temp_item = items[items_letter.index(item)]
                        temp_item.num_constraints += 1

                        first = False
                    else:
                        temp_bags.append(a_letter)

                unary_inclusives.append(UnaryInclusive(item, temp_bags))
            elif count == 5:
                # unary exclusive
                temp_bags = []
                item = 'a'
                first = True
                for a_letter in temp_line:
                    if first:
                        item = a_letter
                        temp_item = items[items_letter.index(a_letter)]
                        temp_item.num_constraints += 1
                        first = False
                    else:
                        temp_bags.append(a_letter)

                unary_exclusives.append(UnaryExclusive(item, temp_bags))
            elif count == 6:
                # binary equals
                binary_equals.append(BinaryEqual([temp_line[0], temp_line[1]]))
                item_one = items[items_letter.index(temp_line[0])]
                item_two = items[items_letter.index(temp_line[1])]
                item_one.num_constraints += 1
                item_two.num_constraints += 1
            elif count == 7:
                # binary does not equal
                binary_not_equals.append(BinaryNotEqual([temp_line[0], temp_line[1]]))
                item_one = items[items_letter.index(temp_line[0])]
                item_two = items[items_letter.index(temp_line[1])]
                item_one.num_constraints += 1
                item_two.num_constraints += 1
            elif count == 8:
                # mutual inclusive
                mutual_inclusives.append(MutualInclusive([temp_line[0], temp_line[1]], [temp_line[2], temp_line[3]]))
                item_one = items[items_letter.index(temp_line[0])]
                item_two = items[items_letter.index(temp_line[1])]
                item_one.num_constraints += 1
                item_two.num_constraints += 1

# start placing things in bags
just_backtrack_file = open("just_backtracking.txt", "w")
print("working on normal backtracking with nothing")
normal_timer = time.perf_counter()
result = backtracking_search(unary_inclusives, unary_exclusives, binary_equals, binary_not_equals, mutual_inclusives,
                             bags, items, "none", just_backtrack_file)
normal_timer_end = time.perf_counter()

just_backtrack_file.close()


if result:
    print("with no heuristic it was solved in " + str(normal_timer_end - normal_timer) + "seconds")
    print_results(bags)
    print("Consistancy checks: ", consistancy_checks)
else:
    print("there is no possible solution for this problem")

reset(bags, items)
consistancy_checks = 0
print("working on MRV_heuristic with degree heuristic")
MRV_file = open("MRV_heuristic.txt", "w")
normal_timer = time.perf_counter()
mrv_result = backtracking_search(unary_inclusives, unary_exclusives, binary_equals, binary_not_equals,
                                 mutual_inclusives,
                                 bags, items, "MRV", MRV_file)
normal_timer_end = time.perf_counter()
MRV_file.close()
#a
if mrv_result:
    print("with the MRV heuristic it was solved in " + str(normal_timer_end - normal_timer) + "seconds")
    print_results(bags)
    print("Consistancy checks: ", consistancy_checks)
else:
    print("there is no possible solution for this problem")

reset(bags, items)

consistancy_checks = 0
print("working on LCV_heuristic with degree heuristic")
LCV_file = open("LCV_heuristic.txt", "w")
normal_timer = time.perf_counter()
lcv_result = backtracking_search(unary_inclusives, unary_exclusives, binary_equals, binary_not_equals,
                                 mutual_inclusives,
                                 bags, items, "LCV", LCV_file)
normal_timer_end = time.perf_counter()
LCV_file.close()

if lcv_result:
    print("with the LCV heuristic it was solved in " + str(normal_timer_end - normal_timer) + "seconds")

    print_results(bags)
    print("Consistancy checks: ", consistancy_checks)
else:
    print("there is no possible solution for this problem")
