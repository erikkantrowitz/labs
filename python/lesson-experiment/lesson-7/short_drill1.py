# List Operations Drill
#
# Objective:
# Practice basic list operations.
#
# Requirements:
# - Given a list of numbers, remove duplicates, sort it, and return the sum
#
import random

# Scaffolding:
def process_list(nums):
    # Your code here
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("This little guy can't handle Letters only numbers")
        
    unique_set = set(nums)    
    sorted_list = sorted(unique_set)
    total = sum(sorted_list)
    return sorted_list, total

#
# Hints:
# - Use set() for duplicates, then list()
#
# Bonus:
# - Handle empty list

# generator of test lists, limiting it to single digits now to make it more likely to get duplicates on smaller lists
def create_random_list(limit):
        random_list = []
        for i in range(limit):
            random_list.append(random.randint(0,9))
        return random_list

test_list_0 = [1, 4, 5, 6, 8, 8, 4, 2, 6]
test_list_1 = create_random_list(12)
test_list_2 = create_random_list(22)
test_list_empty = []
test_list_alpha = ['a','e', 'x', 'y']
test_list_mixed = [9, 'A', 3, 0.5, 7.23, "pod", -4]

print(process_list(test_list_0))
print(process_list(test_list_1))
print(process_list(test_list_empty))
print(process_list(test_list_alpha))
print(process_list(test_list_mixed))