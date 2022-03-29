# string = "HeLLoWorDjDFger"
# res=""
# for char in string:
#      if string.islower():
#          res = res + chr(ord(char)+32)
#      elif string.isupper():
#          res = res + chr(ord(char) - 32)
#      else:
#          res = res + char
# print(res)

#
# s = "hello world"
# count = 0
# for i in s:
#     count+=1
# print(count)

# s = " how are you man"
# words = s.split()
# count= 0
# for i in words:
#     count+=1
# print(count)

# s = " how are you man"
#
# for char in s:
#     if s.count(char)>1:
#         print(char,end = " ")

# a = "hello world"
# duplicates = ""
# non_duplicates = ""
# for char in a:
#     if char not in non_duplicates:
#      non_duplicates = non_duplicates + char
#     elif char in non_duplicates:
#         duplicates = duplicates + char
# print(non_duplicates)
# print((set(duplicates)))

s = "hello world"
char = "l"
for i in range(s):
    if s[i] == char:
        print(i)



