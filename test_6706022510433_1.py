print("\tโปรแกรมคำนวณและบันทึกค่าการเผาผลาญแคลอรี่จากการออกกำลังกาย")
day = int(input("How many days of exercise : "))

running = 0
cycling = 0
swimming = 0

def minute_to_hour(min):
    if min > 60:
        hour = min//60
        minn = min%60
        return {hour:"Hour"},{minn:"Minute"}
    else:
        return {min:"Minute"}
time_running = 0
time_cycling = 0
time_swimming = 0
for i in range(1,day+1):
    print(f"\nDay {i}")
    print("\tExercise type\n1. Running\n2. Cycling\n3. Swimming")
    cate = input("Type of exercise : ")
    minute = int(input("How many minutes do you exercise? : "))
    time = int(input("How many times do you exercise? : "))
    if cate.lower() =="running" or cate == "1":
        running += minute*10*time
        time_running += minute*time

    elif cate.lower() =="cycling" or cate == "2":
        cycling += minute*8*time
        time_cycling += minute*time

    elif cate.lower() =="swimming" or cate == "3":
        swimming += minute*5*time
        time_swimming += minute*time
        
result = running+cycling+swimming

print()
print(f"Calories burned by Running  : {running} calorie")
print(f"Time spent Running : {minute_to_hour(time_running)}")
print()
print(f"Calories burned by Cycling  : {cycling} calorie")
print(f"Time spent Cycling : {minute_to_hour(time_cycling)}")
print()
print(f"Calories burned by Swimming : {swimming} calorie")
print(f"Time spent Swimming : {minute_to_hour(time_swimming)}")
print()
print(f"Total calorie burn : {result}")