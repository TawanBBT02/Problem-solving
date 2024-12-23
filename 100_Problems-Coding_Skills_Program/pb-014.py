def collect_unique_words()->list[str]:
    fruit = ["apple","banana","apple","cherry","date","banana","elderberry"]
    result = []
    for i in fruit:
        if i not in result:
            result.append(i)
    return result

print(collect_unique_words())