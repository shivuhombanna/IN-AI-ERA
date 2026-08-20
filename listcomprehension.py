#traditioonal method 
item=[1,2,3,4,5]
result=[]
for x in item:
    result.append(x+1)
print(result)

# new method 
result=[x+1 for x in item]
print(result)

# list comprehention with condition 
even= [n for n in range(1,11) if n%2==0]
print(even)

prize=[20,50,67,98,88,78]
hight=[p for p in prize if p >=50]
print(hight)

# with if else 
marks=[50,60,70,89,66,47,4,5]
out=["paas" if m>=30 else "fail " for m in marks]
print(out)