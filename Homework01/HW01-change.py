def change(cash,price):
    changes = cash - price
    Chs = 0
    if changes%50 == 10 or changes%50 == 30:
        Chs += (changes%50)+50
        changes -= 50
        bank1000 = changes//1000
        bank500 = (changes%1000)//500
        bank100 = (changes%500)//100
        bank50 = (changes%100)//50
        bank20 = Chs//20

    else:
        bank1000 = changes//1000
        bank500 = (changes%1000)//500
        bank100 = (changes%500)//100
        bank50 = (changes%100)//50
        bank20 = (changes%50)//20


    data = ['bank 1000','bank 500','bank 100','bank 50','bank 20']
    amount = [bank1000,bank500,bank100,bank50,bank20]
    result = dict(zip(data,amount))
    print("Change : ",changes)
    return result

try:
    cash = int(input("cash : "))
    price = int(input("price : "))
    print(change(cash,price))
except ValueError as e:
    print("An error occurred:", e)

