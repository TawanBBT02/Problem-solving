data = [31, 38, 34, 39, 31, 32, 33, 39, 31, 36, 32, 39, 37, 33, 38, 31, 32, 39, 36, 37, 32, 32, 31, 35, 40, 32, 39, 37, 34, 32, 31, 33, 39, 33, 32, 33, 40, 30, 31, 38, 30, 38, 38, 35, 31]

def average(data):
    return sum(data)/45
def median(data:list):
    position = (len(data) + 1)/2
    data.sort()
    return data[int(position)]
def mode(data):
    dict_data = {}
    for i in data:
        if i in dict_data:
            dict_data[i] += 1
        else:
            dict_data[i] = 1
    print(dict_data)
    highest_data = max(dict_data, key=dict_data.get)
    highest_value = dict_data[highest_data]
    return {highest_data:highest_value}
def Range(data):
    return max(data)-min(data)
def Quartile_deviation(data:list):
    data.sort
    Q1 = (data[11] + data[12])/2
    Q3 = (data[34] + data[35])/2
    result = (Q3-Q1)/2
    return result
def standard_deviation(data):
    result = 0
    for i in data:
        result += (i - average(data))**2
    return result/45

print("ค่าเฉลี่ย",average(data))
print("ค่ามัธยฐาน",median(data))
print("ค่าฐานนิยม",mode(data))
print("ค่าพิสัย",Range(data))
print("ส่วนเบี่ยงเบนควอไทล์",Quartile_deviation(data))
print("ส่วนเบี่ยงเบนมาตรฐาน",standard_deviation(data))