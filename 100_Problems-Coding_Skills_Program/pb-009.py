def average_length_of_strings(strings:list[str])->float:
    lengths = []
    Ave_length = 0
    for i in strings:
        lengths.append(len(i))
        Ave_length+=len(i)
    Ave_length/= 5

    return Ave_length 
    
fruit = ["apple","banana","cherry","date","elderberry"]
print(average_length_of_strings(fruit))