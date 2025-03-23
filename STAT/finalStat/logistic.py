import random as rd
D1=[]
data = D1
def create_multi_table():
    n = 10
    k1 = []
    for i in range(n):
        k1.append(rd.randint(5,250))
    k2 = []
    for i in range(n):
        k2.append(rd.randint(15,150))
    k3 = []
    for i in range(n):
        k3.append(rd.randint(30,180))
    k4 = []
    for i in range(n):
        k4.append(rd.randint(20,100))
    k5 = []
    for i in range(n):
        k5.append(rd.randint(0,1))
    
    return [k1,k2,k3,k4,k5]
print(create_multi_table())