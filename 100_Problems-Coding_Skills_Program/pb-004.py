def calculate_sum_and_average() -> None:
    num = []
    for i in range(0,5):
        a = float(input("Enter number %d : " %(i+1)))
        num.append(a)

    sum_num = 0
    for i in num:
        sum_num += i

    sum_ave = sum_num/5

    return f"Sum : {format(sum_num,".2f")} \nAverage : {format(sum_ave,".2f")}"

print(calculate_sum_and_average())