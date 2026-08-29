# def sum_digits(n):
#     print(f"this is input num:  {n}")

#     if n<10:
#         return n

#     return (n%10) + sum_digits(n // 10)

# print(sum_digits(1234798))


# def sum_digits(n):
#     print(f"this is input num:(",n,")")
#     if n<10:
#         print(f"base case reched(",n,")")
#         return n

#     last_digits=n%10
#     remaining=n//10

#     print("last_digits",last_digits)
#     print("remaining",remaining)

#     result=last_digits+sum_digits(remaining)
#     print("returning ",result)
#     return result

# print("Answar",sum_digits(1234))


def recrsive_string(s):
    if len(s)<=1:
        print(s)
        return s
    result=s[-1]+recrsive_string(s[:-1])
    print(result)
    return result
print(recrsive_string("Python"))