import random as rd
import re

D1 = [[48, 38, 47, 41, 21, 38, 28, 23, 29, 32],
        [33, 29, 44, 35, 33, 41, 43, 31, 50, 39], 
        [45, 49, 39, 31, 24, 32, 38, 32, 32, 37], 
        [34, 48, 34, 45, 29, 35, 29, 22, 37, 24], 
        [47, 37, 36, 34, 39, 28, 33, 20, 48, 37]]

D2 = [[18, 19, 35, 23, 33, 20, 40, 41], 
        [14, 12, 40, 29, 25, 23, 27, 25], 
        [24, 40, 24, 18, 27, 44, 39, 21], 
        [35, 13, 36, 45, 13, 27, 41, 40]]

D3 = [[45, 35, 45, 22, 20, 12, 41, 16, 38], 
      [44, 39, 30, 25, 44, 42, 18, 35, 23], 
      [36, 27, 19, 25, 12, 28, 29, 21, 37], 
      [19, 21, 28, 39, 41, 42, 13, 21, 13], 
      [34, 16, 29, 18, 32, 17, 18, 38, 18]]

D4 = [[43, 42, 33, 34, 40, 30, 30, 48, 35], 
      [23, 27, 26, 15, 13, 44, 18, 45, 43], 
      [44, 34, 29, 12, 37, 17, 22, 41, 16], 
      [56, 45, 36, 48, 59, 50, 58, 57, 59], 
      [37, 27, 30, 16, 37, 36, 20, 14, 36]]

D5 = [[41, 36, 38, 43, 49, 29, 56, 52, 31], 
      [27, 48, 55, 32, 33, 40, 47, 30, 41], 
      [44, 51, 56, 52, 31, 43, 36, 51, 56], 
      [57, 43, 53, 46, 38, 43, 50, 25, 42], 
      [35, 42, 33, 35, 50, 44, 60, 25, 47]]

data = D4
n = len(data[0]) * len(data)
k = len(data)
def anova_table():
    data_anova = []
    for  k in range(5):
        num = []
        for i in range(9):
            num.append(rd.randint(25, 60))
        data_anova.append(num)

    return data_anova
#print(anova_table())
def cm(data):
    n = len(data[0]) * len(data)
    sum_data = 0
    for i in data:
        sum_data += sum(i)
    result = (sum_data**2)/n
    return result

def sst(data):
    sum_data = 0
    for i in data:
        for j in i:
            sum_data += j**2
    result = sum_data - cm(data)
    return result

def ssb(data):
    sum_data = 0
    for i in data:
        sum_data += (sum(i)**2)/len(data[0])
    result = sum_data - cm(data)
    return result

def sse(data):
    result = sst(data) - ssb(data)
    return result

def msb(data):
    result = ssb(data)/(k - 1)
    return result

def mse(data):
    result = sse(data)/(n-k)
    return result

def f(data):
    result = msb(data)/mse(data)
    return result

print("CM: ", cm(data))
print("SST: ", format(sst(data), '.2f'))
print("SSB: ", format(ssb(data), '.2f'))
print("SSE: ", sse(data))
print("K - 1: ", len(data) - 1)
print("N - K: ", (len(data[0])*len(data)) - len(data))
print("N - 1: ", (len(data[0])*len(data)) - 1)
print("MSB: ", format(msb(data), '.2f'))
print("MSE: ", format(mse(data), '.2f'))
print("F: ", format(f(data), '.3f'))
print("Critical value: 2.61")
print("Decision: Reject H0")

def detail():
    print("")
    print("Xij & Xij^2 & EXij^2")
    for i in range(len(data)):
        print(sum(data[i]),"&",sum(data[i])**2,"&",sum([j**2 for j in data[i]]))
    print()
    print(sum([sum(j) for j in data]),"&",sum([sum(j) for j in data])**2)
    return ""
print(detail())
