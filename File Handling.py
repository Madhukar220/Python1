import os
os.chdir(r"C:\Users\anand\PycharmProjects\Practice\Files")
# with open("Sample") as fold:
#     count = 0
#     for line in fold:
#         for char in line:
#             count=count+1
# print(count)


####### count the number of words in file###########
# with open("Sample") as fold:
#     count = 0
#     for line in fold:
#         words = line.split()
#         for word in words:
#             count= count+1
# print(count)


######## Print the lines satrting with ovels #########
# with open("Sample") as fold:
#     for line in fold:
#         if line.strip():
#           if line[0] in "aeiouAEIOU":
#             print(line)


######### Print the number of words and line number ########
# with open("Sample") as fold:
#     for line_no,line in enumerate(fold):
#         print(line_no,len(line.split()))

######programme to read the file from the last line #########

# with open("Sample") as fold:
#     list_ = list(fold)
#     for line in list_[::-1]:
#         print(line)

############# count the number of lines without loading the memory ##########

# with open("Sample") as fold:
#     count = 0
#     for line in fold:
#         count+=1
# print(count)


############## To count the number of Spaces in File #################

# with open("Sample") as fold:
#     ch = " "
#     count = 0
#     for line in fold:
#         for char in line:
#          if char == ch:
#             count+=1
# print(count)

####  OR ###########
# with open("Sample") as fold:
#     count = 0
#     for line in fold:
#         count+=line.count(" ")
# print(count)

############# create dictionary with each word and its count ###############
# with open("Sample") as fold:
#     d = {}
#     for line in fold:
#         words = line.split()
#         for word in words:
#             if line.strip():
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word]+=1
# print(d)

############# Most occuring word in the file ###############
#
# with open("Sample") as fold:
#     d = {}
#     res = ""
#     for line in fold:
#         words = line.split()
#         for word in words:
#             if word not in d:
#                d[word] = 1
#             else:
#                 d[word] +=1
# # print(d)
# least,*rest,most= sorted(d.items(),key=lambda item:item[-1])
#
# print(most)


########### Print the nth line ###############
# with open("Sample") as fold:
    # n = 5
    # count = 0
    # for line in fold:
    #     count+=1
    #     if count == n:
    #        print(line)

with open("Sample") as fold:
  for line_no,line in enumerate(fold):
      if line_no < 5:
          print(line)












