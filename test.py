# print("โปรแกรมเพื่อเก็บคะแนนวิชา Problem Solving")
# Nstd = int(input("ระบุจํานวนนักศึกษา : "))
# result = {}
# for i in range(Nstd):
#     name = input("ชื่อ : ")
#     score = int(input("ระบุคะแนน : "))
#     result[name] = score

# print("--Unsorted Score--")
# for i in result:
#     print(i,":",result[i])

# รับจำนวนของนักศึกษา
num_students = int(input("Enter the number of students: "))

# สร้างรายการสำหรับเก็บข้อมูลชื่อและคะแนน
students = []

for _ in range(num_students):
    name = input("Enter student name: ")
    score = float(input(f"Enter student score for {name}: "))
    students.append((name, score))

# แสดงคะแนนที่ยังไม่ได้เรียงลำดับ
print("\n--Unsorted Scores--")
for name, score in students:
    print(f"{name}: {score}")

print(students)