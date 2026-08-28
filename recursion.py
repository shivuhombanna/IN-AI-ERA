# def count_loop(n):
#     for i in range(n,0,-1):
#         print(i)

#     print("Done!")

# count_loop(6)


# def count(n):
#     if n==0:
#         print("done!")
#         return
#     print(n)
#     count(n-1)

# count(7)

# def neted(data):
#     total=0
#     for item in data:
#         if isinstance(item,list):
#             total+=neted(item)
#         else:
#             total+=item
#     return total
# print(neted([1,[2,[3,[4,[5]]]]]))


#factorial 
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(3))
