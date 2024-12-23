def store_student_scores(student_data:list[tuple[str,str,float]])->dict[str,dict[str,float]]:
    result = {}
    for i in range(len(student_data)):
        result[student_data[i][0]] = {"name":student_data[i][1],"score":student_data[i][2]}
    
    return result

std_data = [
    ("123456","Alice",85.5),
    ("654321","Bob",92.0),
    ("112233","Charlie",78.0)
]
print(store_student_scores(std_data))