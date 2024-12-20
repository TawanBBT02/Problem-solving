def contains_vowel(s:str)->bool:
    vowel = ["a","e","i","o","u"]
    words = []
    for i in s:
        words.append(i)
    result = []
    for i in words:
        if i in vowel:
            #result.append(i)
            return True
        elif i not in vowel:
            continue
        else:  
            return False

    # if result != 0:
    #     return True
    # else:
    #     return False


print(contains_vowel("Hello World"))