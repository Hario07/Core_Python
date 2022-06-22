sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
# print(set3)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

a = set1.union(set2)
print(a)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30}
set2 = {20, 40, 50}
a = set1.difference(set2)
print(a)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)
print(set3)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("No comman data")
else:
    print("The comman elemnet is:")
    print(set1.intersection(set2))

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)

# print(---------------------------------------------------------------------------------------------->)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)

# print(---------------------------------------------------------------------------------------------->)