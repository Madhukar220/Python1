l = [2,6,8,20]
# def square(sequence):
#     for i in l:
#         yield i**2
#
# res = square(l)
# print(list(res))

#####  Generator Function ###########
# square = (i**2 for i in l)
# print(list(square))


# l = ["bob", "Steve", "Harvey", "Kellen", "Kavin"]
# def odd(sequence):
#     for item in sequence:
#         if len(item) % 2 == 1:
#             yield item
#
# print(list(odd(l)))


#####  Generator Function ###########
# odd = (item for item in l if len(item)%2==1)
# print(list(odd))




