print("โปรแกรมเพื่อเก็บคะแนนวิชา Problem Solving")
Nstd = int(input("ระบุจํานวนนักศึกษา : "))
result = {}
for i in range(Nstd):
    name = input("ชื่อ : ")
    score = int(input("ระบุคะแนน : "))
    result[name] = score

print("--Unsorted Score--")
for i in result:
    print(i,":",result[i])
 