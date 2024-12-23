print("โปรแกรมออมเงิน")
a = int(input("จำนวนเงินที่ต้องการออม : "))
type = int(input("\n1.รายวัน\n2.รายเดือน\nรูปแบบการออม :"))
years = int (input("จำนวนปีที่จะออม : "))
if type =="1":
    result = a// ( 365 * years)

else :
    result = a// ( 12 * years)

print(f"จำนวนเงินที่ต้องออมในแต่ละครั้ง : {result}")