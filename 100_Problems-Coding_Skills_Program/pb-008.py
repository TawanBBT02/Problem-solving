def separate_by_index(s:str)->tuple[str,str]:
    even_str = ""
    odd_str = ""
    for i in range(len(list(s))):
        if i%2 ==0:
            even_str+=(s[i])
        else:
            odd_str+=(s[i])

    return  even_str,odd_str
    
print(separate_by_index("Hello World"))