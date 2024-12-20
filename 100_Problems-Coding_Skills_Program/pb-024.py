def student_info(student_data: list[tuple[str,str]])-> dict[str,str]:
    result = {}
    for i in range(len(student_data)):
        result[student_data[i][0]] = student_data[i][1]
    
    return result

std_data =[("123456","Alice"),("654321","Bob"),("112233","Charlie")]
print(student_info(std_data))