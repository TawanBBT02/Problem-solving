def reverse_string(s:str)->str:
    words = []
    for i in s:
        words.append(i)

    words.reverse()
    result = ""
    for i in words:
        result+=i
    
    return result

print(reverse_string("Hello World"))