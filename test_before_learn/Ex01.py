print("***calcilate sum of odd and even number (Exit press 0)***")
sum_even = 0
sum_odd = 0

while(True):
    num = int(input("Enter number : "))
    if num == 0:
        break
    elif num%2 ==0:
        sum_even += num
    elif num%2 !=0: 
        sum_odd += num 


print(f"sum of even numbers = {sum_even}")
print(f"sum of odd numbers = {sum_odd}")