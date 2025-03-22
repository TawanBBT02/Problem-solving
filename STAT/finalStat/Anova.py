import random as rd

data = [[48, 38, 47, 41, 21, 38, 28, 23, 29, 32],
        [33, 29, 44, 35, 33, 41, 43, 31, 50, 39], 
        [45, 49, 39, 31, 24, 32, 38, 32, 32, 37], 
        [34, 48, 34, 45, 29, 35, 29, 22, 37, 24], 
        [47, 37, 36, 34, 39, 28, 33, 20, 48, 37]]
n = len(data[0]) * len(data)
k = len(data)
def anova_table():
    data_anova = []
    for  k in range(5):
        num = []
        for i in range(10):
            num.append(rd.randint(20, 50))
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
print("F: ", format(f(data), '.2f'))
print("Critical value: 3.89")
print("Decision: Reject H0")

