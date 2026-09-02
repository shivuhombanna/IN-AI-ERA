students = [
    {"name": "Alice", "score": 85, "grade": "B"},
    {"name": "Bob", "score": 92, "grade": "A"},
    {"name": "Charlie", "score": 45, "grade": "F"},
    {"name": "Diana", "score": 78, "grade": "C"},
    {"name": "Eve", "score": 95, "grade": "A"},
    {"name": "Frank", "score": 62, "grade": "D"}
]
# sort_stu=sorted(students,key=lambda x: x["name"], reverse=False)
# print(sort_stu)


# # filter functio
# filtersw=list(filter(lambda x: x["score"] >=70, students))
# print(filtersw)

ext_name=list(map(lambda x: x["name"] , students))
print(ext_name)