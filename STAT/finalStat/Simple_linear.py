import random as rd
import math
D1 = [[24, 30, 26, 15, 16, 27, 30, 15, 24, 27], [20, 22, 13, 22, 27, 15, 15, 22, 22, 17]]
D2 = [[38, 39, 18, 22, 26, 30, 28, 42, 25, 38], [24, 40, 23, 26, 16, 17, 34, 27, 26, 29]]
data = D2
def sim_table():
    data = []
    for  k in range(2):
        num = []
        for i in range(10):
            num.append(rd.randint(15, 45))
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
    result = ((1/(n-1))*(x_y - ((x*y)/n)))/(standard_deviation(data[0])*standard_deviation(data[1]))

    return result

print("R :",r_power_2(data))
print("R^2 :",r_power_2(data)**2)  

def b(data):
    xy = 0
    for i in range(len(data[0])):
        xy += data[0][i] * data[1][i]
    x = sum(data[0])
    y = sum(data[1])
    x_2 = 0
    for i in range(len(data[0])):
        x_2 += data[0][i]**2
    result = (((n*(xy)) - (x*y)))/((n*(x_2)) - (x**2))
    return result

def a(data):
    result = (sum(data[1])/n) - (b(data)*(sum(data[0])/n))
    return result

print(f"Y = {format(a(data), '.2f')} + {format(b(data), '.3f')}X ")

print("X = ",sum(data[0]))
print("Y = ",sum(data[1]))
print("X^2 = ",sum([i**2 for i in data[0]]))
print("Y^2 = ",sum([i**2 for i in data[1]]))
print("XY = ",sum(data[0][i]*data[1][i] for i in range(len(data[0]))))
print(f"S.D.X = {format(standard_deviation(data[0]), '.4f')}")
print(f"S.D.Y = {format(standard_deviation(data[1]), '.4f')}")