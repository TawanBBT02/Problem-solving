class Students:
    def __init__(self,capacity):
        self.capacity = capacity
        self.num = [None] * capacity

    def AddStd(self,name,score):
        self.name = name
        self.score = score


Nstd = int(input("Enter the number of students: "))
std = Students(Nstd)
for i in range(Nstd):
    name = input("Enter student name: ")
    score = float(input(f"Enter student score for {name}: "))
    std.AddStd(name,score)

print(std.num)