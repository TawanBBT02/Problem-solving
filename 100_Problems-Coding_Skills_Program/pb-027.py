def build_set()->set[int]:
    result = []
    for i in range(0,5):
        add = int(input("User enters : "))
        result.append(add)

    return set(result)
print(build_set())