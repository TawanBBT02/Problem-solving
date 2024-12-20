def count_word_occurrences(words: list[str])->dict[str,int]:
    result = {}
    for i in words:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result


fruit = ["apple","banana","apple","orange","banana","apple"]
print(count_word_occurrences(fruit))