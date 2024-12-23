def set_operations(set1:set,set2:set)-> tuple[set,set]:
    result = (set1.difference(set2),set2.difference(set1))
    return result


set1 = {'a','b','c'}
set2 = {'b','c','d'}
print(set_operations(set1,set2))