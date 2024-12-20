def remove_word(sentence:str,word_to_remove:str)-> str:
    result = ""
    for i in sentence.split():
        print(i)
        if i == word_to_remove:
            continue
        else:
            result += i
            result += " "

    return str(result)


sen = "Python is a popular programming language."
word_t_remove = "popular"
print(remove_word(sen,word_t_remove))