def character_frequency(*args: str)->dict:
    words = ""
    for i in args:
        words+=i
    print(words)
    char = {}
    for i in words:
        if i not in char:
            char[i] = 1
        else:
            char[i] += 1
    return char



print(character_frequency("hello","world","test","case","example"))