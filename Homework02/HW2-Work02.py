def cal_grade(hour,pay_rate):
    if hour > 160:
        salary = (160 * pay_rate) + ((hour - 160) * (pay_rate * 1.5))
    else :
        salary = hour * pay_rate

    return salary
    
print("โปรแกรมคํานวณเงินเดือน")
emp = int(input("Enter the number of students : "))
for employee in range(0,emp):
    print(f"\t---Employee {employee+1}---")
    hour = int(input("Enter Hours : "))
    pay_rate = int(input("Enter Pay rate : "))
    salary = cal_grade(hour,pay_rate)
    print(f"Your Grade is {salary} \n")
print("\t---End of Program---")