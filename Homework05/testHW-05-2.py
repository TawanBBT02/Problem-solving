class Student_information:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append((name, score))

    def display_students(self):
        print("\n--Unsorted Scores--")
        for name, score in self.students:
            print(f"{name}: {score}")

    def sort_students(self):
        for i in range(len(self.students)):
            for j in range(len(self.students) - i - 1):
                if self.students[j][1] < self.students[j + 1][1]:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]

    def display_sorted_students(self):
        print("\n--Sorted Scores (Bubble Sort)--")
        for name, score in self.students:
            print(f"{name}: {score}")

    def display_top_scores(self, top_n=3):
        print(f"\n--Top {top_n} Highest Scores--")
        for name, score in self.students[:top_n]:
            print(f"{name}: {score}")

    def display_bottom_scores(self):
        print(f"\n--Top 3 Lowest Scores--")
        for name, score in self.students[-1:-4:-1]:
            print(f"{name}: {score}")

    def search_by_score(self, score_to_search):
        found_students = [name for name, score in self.students if score == score_to_search]
        if found_students:
            print(f"Found student(s) with score {score_to_search}")
        else:
            print(f"No students found with score {score_to_search}")


if __name__ == "__main__":
    Student = Student_information()
    Nstd = int(input("Enter the number of students: "))

    for _ in range(Nstd):
        name = input("Enter student name: ")
        score = float(input(f"Enter student score for {name}: "))
        Student.add_student(name, score)

    Student.display_students()
    Student.sort_students()
    Student.display_sorted_students()
    Student.display_top_scores()
    Student.display_bottom_scores()

    while True:
        search_score = input("\nEnter the score to search (or type 'exit' to quit): ")
        if search_score.lower() == 'exit':
            break
        Student.search_by_score(float(search_score))
