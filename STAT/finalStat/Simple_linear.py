import random as rd
import math
data = [[24, 30, 26, 15, 16, 27, 30, 15, 24, 27], [20, 22, 13, 22, 27, 15, 15, 22, 22, 17]]
#data = [[1,1,2,3,5],[2,2.5,3,3.5,4]]
def sim_table():
    data = []
    for  k in range(2):
        num = []
        for i in range(10):
            num.append(rd.randint(10, 30))
        data.append(num)

    return data
#print(sim_table())
n = len(data[0])
def standard_deviation(data):
    rog = 0
    ave = sum(data)/len(data)
    for i in data:
        rog += (i - ave)**2
    rog = rog/(len(data) - 1)
    result = math.sqrt(rog)
    return result

def r_power_2(data):
    x_y = 0
    for i in range(len(data[0])):
        x_y += data[0][i] * data[1][i]
    x = sum(data[0])
    y = sum(data[1])
    print(x_y, x, y)
    result = ((1/(n-1))*(x_y - ((x*y)/n)))/(standard_deviation(data[0])*standard_deviation(data[1]))

    return result

print("R :",r_power_2(data))
print("R^2 :",r_power_2(data)**2)
