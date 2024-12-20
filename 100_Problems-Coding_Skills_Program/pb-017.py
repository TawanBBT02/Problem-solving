def is_word_in_list(word_list:list[str],search_term:str)->bool:
    if search_term in word_list:
        return True
    else:
        return False

word_list = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon"]
print(is_word_in_list(word_list,"cherry"))
print(is_word_in_list(word_list,"mango"))