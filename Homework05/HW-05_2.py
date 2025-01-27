# รับจำนวนของนักศึกษา
num_students = int(input("Enter the number of students: "))

# สร้างรายการสำหรับเก็บข้อมูลชื่อและคะแนน
students = []

# รับข้อมูลนักศึกษา
for _ in range(num_students):
    name = input("Enter student name: ")
    score = float(input(f"Enter student score for {name}: "))
    students.append((name, score))

# แสดงคะแนนที่ยังไม่ได้เรียงลำดับ
print("\n--Unsorted Scores--")
for name, score in students:
    print(f"{name}: {score}")

# จัดเรียงคะแนนจากมากไปน้อย (Bubble Sort)
for i in range(len(students)):
    for j in range(len(students) - i - 1):
        if students[j][1] < students[j + 1][1]:
            students[j], students[j + 1] = students[j + 1], students[j]

# แสดงคะแนนที่จัดเรียงแล้ว
print("\n--Sorted Scores (Bubble Sort)--")
for name, score in students:
    print(f"{name}: {score}")

# แสดง Top 3 คะแนนสูงสุด
print("\n--Top 3 Highest Scores--")
for name, score in students[:3]:
    print(f"{name}: {score}")

# แสดง Top 3 คะแนนต่ำสุด
print("\n--Top 3 Lowest Scores--")
for name, score in students[-3:]:
    print(f"{name}: {score}")

# ฟังก์ชันค้นหานักศึกษาตามคะแนน
def search_by_score(score_to_search):
    found_students = [name for name, score in students if score == score_to_search]
    if found_students:
        print(f"Found student(s) with score {score_to_search}: {', '.join(found_students)}")
    else:
        print(f"No students found with score {score_to_search}")

# ค้นหาคะแนนจากผู้ใช้
while True:
    search_score = input("\nEnter the score to search (or type 'exit' to quit): ")
    if search_score.lower() == 'exit':
        break
    search_by_score(float(search_score))