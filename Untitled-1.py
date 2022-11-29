list1=list(map(int,input("list:").split(",")))
print(list1)
list1=[x**3 for x in list1 if x>10]
print(list1)