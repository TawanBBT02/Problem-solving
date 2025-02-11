my_dict = {'Dave':'001','Ava':'002','Joe':'003'}
print(my_dict)
print(type(my_dict))

my_dict = dict()
print(my_dict)
print(type(my_dict))

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
x = my_dict["country"]
print(x)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
x = my_dict.get("country")
print(x)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
x = my_dict.keys()
print(x)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
x = my_dict.keys()
print(x) #before the change
my_dict["color-like"] = "white"
print(my_dict)
print(x) #after the change

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
if "country" in my_dict:
    print("Yes, 'country' is one of the keys in the my_dict dictionary")
    
my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
my_dict["name"] = "Ford"
my_dict["color-like"] = "Blue"
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
my_dict.update({"country": "Thailand"})
my_dict.update({"color-like": "Green"})
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
my_dict.pop("age")
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
my_dict.popitem()
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
my_dict.clear()
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
for x in my_dict:
    print(x)
    
my_dict = dict(name = "John", age = 36, country = "Norway")
for x in my_dict:
    print(my_dict[x])    
my_dict = dict(name = "John", age = 36, country = "Norway")
for x in my_dict.values():
    print(x)
for x in my_dict.keys():
    print(x)
for x, y in my_dict.items():
    print(x, y)
    
my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
new_dict1 = my_dict.copy()
print(new_dict1)
new_dict2 = dict(my_dict)
print(new_dict2)