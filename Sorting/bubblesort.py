def bubbleSoet(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before : ",data)
bubbleSoet(data)
print("Bubble Sort : ",data)
