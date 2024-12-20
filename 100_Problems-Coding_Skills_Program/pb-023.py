def create_dictionnary(tuple1:tuple[int,...],tuple2:tuple[str,...])->dict[int,str]:
    result = {}
    for i in range(len(tuple1)):
        result[tuple1[i]] = tuple2[i]
    return result

tuple1 = [1,2,3,4]
tuple2 = ["ant","cat","dog","cow"]
print(create_dictionnary(tuple1,tuple2))