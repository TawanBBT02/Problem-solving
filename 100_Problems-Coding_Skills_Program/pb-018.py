def remove_word_from_list(words: list[str],word:str)-> list[str]:
    words.remove(word)
    return words

words = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon"]
word = "cherry"
print(remove_word_from_list(words,word))