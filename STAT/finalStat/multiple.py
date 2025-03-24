import random as rd
D1=[]
data = D1
def create_multi_table():
    n = 10
    k1 = []
    for i in range(n):
        k1.append(rd.randint(5,200))
    k2 = []
    for i in range(n):
        k2.append(rd.randint(15,150))
    k3 = []
    for i in range(n):
        k3.append(rd.randint(30,175))
    k4 = []
    for i in range(n):
        k4.append(rd.randint(20,50))
    k5 = []
    for i in range(n):
        k5.append(rd.randint(10,70))
    
    return [k1,k2,k3,k4,k5]
print(create_multi_table())

def create_multi_table_final():
    n = 10
    k1 = []
    for i in range(n):
        k1.append(rd.randint(5,200))
    k2 = []
    for i in range(n):
        k2.append(rd.randint(15,100))
    k3 = []
    for i in range(n):
        k3.append(rd.randint(30,90))
    k4 = []
    for i in range(n):
        k4.append(rd.randint(20,50))
    k5 = []
    for i in range(n):
        k5.append(rd.randint(10,70))
    k6 = []
    for i in range(n):
        k6.append(rd.randint(7,80))
    
    return [k1,k2,k3,k4,k5,k6]
#print(create_multi_table_final())