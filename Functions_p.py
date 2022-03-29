###########to count the number of positional and keyword arguments#########
# def display(*args, **kwargs):
#     print(len(args))
#     print(len(kwargs))
#
#
# display(1, 2, 3, a=1, b=2, c=3, d=40)

###########Function to creat list of 1 to 10 even numbers#########

# def even():
#     l = []
#     for i in range(1,11):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# print(even())

###########Function to create a dictionary with its count and word pair#########

# def element(sequence):
#     d =  {}
#     for i in sequence:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] = d[i]+1
#     return d
#
#
# print(element(["hello", "how", "how", "are", "are", "you"]))


###########Function to creat list of first 5 prime numbers#########

# def prime_num(n):
#     l = []
#     count = 0
#     num = 0
#     while count<n:
#         if num > 1:
#             for i in range(2,num):
#                 if num % i == 0:
#                     break
#             else:
#                 count = count + 1
#                 l.append(num)
#         num = num+1
#     return l
#
#
# print(prime_num(6))

###########Function to check the given number is prime or not#########

# def prime_n(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print("the given number is not a prime number")
#             break
#     else:
#         print("The given number is aprime number")
#
#
# prime_n(7)

###########Function to return last digit of any numbers#########

# def last(num):
#     x = str(int(num))
#     y = x[-1]
#     z = int(str(y))
#     return z
# print(last(54687))

###########Function to return last digit of any numbers#########

# def lst(num):
#     x = num % 10
#     return x
#
#
# print(lst(56489))

# def tail(sequence):
#     x = list(sequence[-3:])
#     return x
#
# print(tail(("hello", 2)))

###########Function to return only list of elements which are starting from ovels#########

# def ovels(sequence):
#     l = []
#     for i in sequence:
#         if i[0] in "aeiouAEIOU":
#             l.append(i)
#     return l
#
#
# print(ovels(["hello" , "is", "My", "Own", "Car"]))

