def cal_grade(score):
    if 0 <= score <= 100 :

        if score >= 80:
            Grade = "A"
        elif score >= 75:
            Grade = "B+"
        elif score >= 70:
            Grade = "B"
        elif score >= 65:
            Grade = "C+"
        elif score >= 60:
            Grade = "C"
        elif score >= 55:
            Grade = "D+"
        elif score >= 50:
            Grade = "D"
        elif score < 50:
            Grade = "F"

        return Grade

    else :
        print("Error!!")
        return None
    
print("โปรแกรมคํานวณเกรด")
std = int(input("Enter the number of students : "))
for student in range(0,std):
    print(f"\t---Number {student+1}---")
    score = int(input("Enter Score : "))
    Grade = cal_grade(score)
    print(f"Your Grade is {Grade} \n")
print("\t---End of Program---")