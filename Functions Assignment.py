# def fibo(n):
#     a = 0
#     b = 1
#     while a <= n:
#         if a == n:
#             return "the given number is a fibonacci number"
#
#         c = a + b
#         a = b
#         b = c
#     return "the given number is not a fibonacci number"
#
#
# print(fibo(34))


# s = "hello"
#
# def power(sequence):
#     d = {}
#     for index,item in enumerate(sequence):
#         d[item]  = index
#     print(d)
#
#
# power(s)

# def palin(string):
#     if string == string[::-1]:
#         return "the given string is pallindrome"
#     else:
#         return "it is not aprime number"
#
#
# print(palin("mjmk"))


l = ["are", "dad", "how", "mom"]
#
def palin(word):
    for i in word:
         if i == i[::-1]:
            print("all the strings present in the list are pallindrome")

    else:
     print("all the string present in the list are not pallindrome")


palin(l)










