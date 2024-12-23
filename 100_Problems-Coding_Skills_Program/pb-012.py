def replace_characters(s:str)->str:
    words = []
    for i in s:
        words.append(i)
    result = ""
    for word in words:
        if word == "a":
            result+="@"
        elif word == "l":
            result+="1"
        elif word == "o":
            result+="0"
        else:
            result+=word
    return result

print(replace_characters("Hello World"))