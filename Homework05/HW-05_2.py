Nstd = int(input("Enter the number of students: "))
students = []
for _ in range(Nstd):
    name = input("Enter student name: ")
    score = float(input(f"Enter student score for {name}: "))
    students.append((name, score))
    
print("\n--Unsorted Scores--")
for name, score in students:
    print(f"{name}: {score}")

for i in range(len(students)):
    for j in range(len(students) - i - 1):
        if students[j][1] < students[j + 1][1]:
            temp = students[j]
            students[j]  =  students[j + 1] 
            students[j + 1] = temp
            

print("\n--Sorted Scores (Bubble Sort)--")
for name, score in students:
    print(f"{name}: {score}")

print("\n--Top 3 Highest Scores--")
for name, score in students[:3]:
    print(f"{name}: {score}")

print("\n--Top 3 Lowest Scores--")
for name, score in students[-1:-4:-1]:
    print(f"{name}: {score}")

def search_by_score(score_to_search):
    found_students = [name for name, score in students if score == score_to_search]
    if found_students:
        print(f"Found student with score {score_to_search}: {', '.join(found_students)}")
    else:
        print(f"No students found with score {score_to_search}")

while True:
    search_score = input("\nEnter the score to search (or type 'exit' to quit): ")
    if search_score.lower() == 'exit':
        break
    search_by_score(float(search_score))