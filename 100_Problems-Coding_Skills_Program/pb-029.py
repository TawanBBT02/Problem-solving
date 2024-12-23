def set_operations(set1:set,set2:set)-> tuple[set,set]:
    result = (set1.union(set2),set1.intersection(set2))
    return result


set1 = {'a','e','i','o','u'}
set2 = {'h','e','l','l','o'}
print(set_operations(set1,set2))