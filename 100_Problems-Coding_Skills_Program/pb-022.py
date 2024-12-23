def create_dictionnary(list1:list[int],list2:list[str])->dict[int,str]:
    result = {}
    for i in range(len(list1)):
        result[list1[i]] = list2[i]
    return result

list1 = [1,2,3,4]
list2 = ["blue","green","pink","yellow"]
print(create_dictionnary(list1,list2))




# # ตัวอย่าง 2 list
# keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'Bangkok']

# # ใช้ zip() เพื่อจับคู่ key กับ value และสร้าง dict
# my_dict = dict(zip(list1, list2))

# print(my_dict)

# my_dict = {}
# for i in range(len(list1)):
#     my_dict[list1[i]] = list2[i]

# print(my_dict)