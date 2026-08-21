# squries={n: n**2 for n in range(1,9)}
# print(squries)

# list=[ n for n in range(1,10) if 1**n]

# item=["rice","dal","chilly","tamato"]
# prize=[150,87,87,67,99]
# prize_map={item: prize for item,prize in zip(item,prize) if prize>=100}
# print(prize_map)

# marks={"mahadev":77, "shivaraj":98, "amaresh":34}
# result={name: "pass" if score>=35 else "fail" for name,score in marks.items()}
# print(result)

# froutes=["apple","banna","cherry","kolaka"]
# index={i: froutes for i ,froutes in enumerate(froutes)}
# print(index)

# inverting a dictionari
original={"a":1,"b":2,"c":3}
invert={v: k for k, v in original.items()}
print(invert)

#nested comp
row=[[1,2],[3,4]]
flat=[n for row in row for n in row]
print(flat)

