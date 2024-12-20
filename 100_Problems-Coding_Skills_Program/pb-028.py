def check_membership(s:set,value:str)-> bool:
    if value in s:
        return True
    elif value not in s :
        return False

s = {1,2,3,'a','e','i','o','u',"red","green","blue"}
print(check_membership(s,2))
print(check_membership(s,"a"))
print(check_membership(s,"yellow"))