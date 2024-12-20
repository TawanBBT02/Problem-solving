def insert_at_front(words: list[str])->list[str]:
    result = []
    for i in words:
        result.insert(0,i)

    return result

fruit = ["apple","banana","cherry"]
print(insert_at_front(fruit))