def calculate_statistics(t:tuple[int,...])->tuple[tuple[int,...],int,int,int,float]:
    Squared_Values = []
    max_val = 0
    min_val = 0
    sum_val = 0
    for i in t:
        Squared_Values.append(i**2)
        sum_val += i**2
    
    max_val = max(Squared_Values)
    min_val = min(Squared_Values)

    Average = sum_val/len(t)

    return tuple(Squared_Values),max_val,min_val,sum_val,Average

Input = (1,2,3,4,5,6,7,8,9,10)
print(calculate_statistics(Input))